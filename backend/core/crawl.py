import asyncio
from collections import OrderedDict
import json
import re
import jieba
import aiohttp
import uuid
import string
import stopwords as sw
from lxml import etree, html
from playwright.async_api import async_playwright, expect

# sqlalchemy
from sqlalchemy import select, or_, false, true
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

# Sql Related
from sql import models as sqlmd
from sql.engine import general as engine

from models.exceptions import RecordNotExist

from models.store import MovieStatsModel
async def run(token):
    # 开始爬虫 添加crawler表信息
    await start_crawl(token)
    print('添加爬虫表')
    # 定义select
    stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())\
            .options(selectinload(sqlmd.StoreRecord.crawl))
    wish, do, collect = [],[],[]
    # 开始爬虫
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://accounts.douban.com/passport/login")
        await page.locator(".quick").first.click()
        # 等待二维码出现
        await page.wait_for_selector(".account-qr-scan img")
        # 抓取二维码 URL
        c = await page.content()
        tree = etree.HTML(c.encode())
        qr_code_element = tree.xpath('//div[@class="account-qr-scan"]/img')[0]
        qr_code_url = qr_code_element.get('src')
        print('抓取二维码', qr_code_url)
        # url储存到数据库
        async with AsyncSession(engine) as session:
            orm_record = (await session.execute(stmt)).scalar_one_or_none()
            if orm_record is None:
                raise RecordNotExist()
            orm_record.crawl.qrcode_url = qr_code_url
            await session.commit()
        print('存入数据库')
        # 等待扫描, 1分钟timeout
        await page.wait_for_selector('//li[@class="account-tab-scan"]', timeout=60000 ,state="hidden")
        # 改变状态 进入progress 1
        async with AsyncSession(engine) as session:
            orm_record = (await session.execute(stmt)).scalar_one_or_none()
            if orm_record is None:
                raise RecordNotExist()
            orm_record.crawl.running = 1
            await session.commit()
        # 跳转到个人主页
        await page.goto("https://movie.douban.com/mine")
        await page.wait_for_load_state(state='load')
        # 屏幕快照
        file_name = str(uuid.uuid4())
        await page.screenshot(path=f'../screenshots/{file_name}.png')
        print('截取快照')
        # 获取用户名
        c = await page.content()
        tree = etree.HTML(c.encode())
        username = tree.xpath('//li[@class="nav-user-account"]/a/span/text()')[0]
        print('获取用户名')
        # 跳转到已看
        await page.goto("https://movie.douban.com/mine?status=collect")
        await page.wait_for_load_state(state='load')
        print('开始爬已看')
        # While循环每一页
        while True:
            c = await page.content()
            tree = etree.HTML(c)
            ids = tree.xpath('//li[@class="title"]/a/@href')
            for i in ids:
                i = str(i).replace('https://movie.douban.com/subject/', '').replace('/', '')
                collect.append(i)
                # 判断有没有下一页
            if tree.xpath('//span[@class="next"]/a/@href') == []:
                break
            await page.get_by_role("link", name="后页>").click()
        # 跳转到想看
        await page.goto("https://movie.douban.com/mine?status=wish")
        await page.wait_for_load_state(state='load')
        print('开始爬想看')
        while True:
            c = await page.content()
            tree = etree.HTML(c)
            ids = tree.xpath('//li[@class="title"]/a/@href')
            for i in ids:
                i = str(i).replace('https://movie.douban.com/subject/', '').replace('/', '')
                wish.append(i)
            if tree.xpath('//span[@class="next"]/a/@href') == []:
                break
            await page.get_by_role("link", name="后页>").click()
        # 跳转到在看
        await page.goto("https://movie.douban.com/mine?status=do")
        await page.wait_for_load_state(state='load')
        print('开始爬在看')
        while True:
            c = await page.content()
            tree = etree.HTML(c)
            ids = tree.xpath('//li[@class="title"]/a/@href')
            for i in ids:
                i = str(i).replace('https://movie.douban.com/subject/', '').replace('/', '')
                do.append(i)
            if tree.xpath('//span[@class="next"]/a/@href') == []:
                break
            await page.get_by_role("link", name="后页>").click()
        # 关闭playwright
        await context.close()
        await browser.close()
    # 改变状态 进入progress 2
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        orm_record.crawl.running = 2
        await session.commit()
    # 爬取电影信息
    print("开始爬在看电影信息")
    for id in do: await crawl_movie(id)
    print("开始爬想看电影信息")
    for id in wish: await crawl_movie(id)
    print("开始爬看过电影信息")
    collect_list = [await crawl_movie(id) for id in collect]
    print("开始处理可视化数据")
    #爬取可视化十局
    await process_data(collect_list, token)
    # 改变状态 进入progress 3
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        orm_record.crawl.running = 3
        await session.commit()
    # 将信息存入Douban表
    await end_crawl(token, wish, do, collect, file_name, username)



def run_sync_main(token):
    # 将异步函数转换为同步函数
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run(token))

async def start_crawl(token: str):
    new_crawl = sqlmd.Crawler(
        qrcode_url=None
    )
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        session.add(new_crawl)
        await session.flush()
        orm_record.c_id = new_crawl.id
        await session.commit()
    
async def end_crawl(token: str, do: list, wish: list, collect: list, filename: str, username: str):
    new_douban = sqlmd.Douban(
        screenshot=filename,
        douban_id=username,
        wish=",".join(wish),
        do=",".join(do),
        collect=",".join(collect),
    )
    stmt = select(sqlmd.StoreRecord)\
        .filter(sqlmd.StoreRecord.token == token)\
        .filter(sqlmd.StoreRecord.deleted == false())\
        .options(selectinload(sqlmd.StoreRecord.crawl))\
        .options(selectinload(sqlmd.StoreRecord.douban))
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        # 添加douban仓库信息
        session.add(new_douban)
        await session.flush()
        # 更新爬虫状态
        orm_record.crawl.running = 4
        # 添加user外键
        orm_record.d_id = new_douban.id
        # 更新记录状态完成
        orm_record.completed = True
        await session.commit()

async def crawl_movie(douban_id: int):
    # 先看数据库有没有
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.Movie)\
            .filter(sqlmd.Movie.douban_id == douban_id)\
            .filter(sqlmd.Movie.deleted == false())
        orm_movie = (await session.execute(stmt)).scalar_one_or_none()
        if orm_movie is not None: return orm_movie.__dict__
    url = f"https://movie.douban.com/subject/{douban_id}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_text = await response.text()
            tree = html.fromstring(html_text)
    # 处理信息
    new_movie = await handleText(tree, douban_id)
    async with AsyncSession(engine) as session:
        session.add(new_movie)
        await session.commit()
    return new_movie.__dict__


async def handleText(tree, douban_id):
    # 获取电影名字
    name_nodes = tree.xpath('//div[@id="content"]/h1/span[@property="v:itemreviewed"]')
    name = name_nodes[0].text.strip() if name_nodes else None

    # 获取年代
    year_nodes = tree.xpath('//div[@id="content"]/h1/span[@class="year"]')
    year_str = year_nodes[0].text.strip() if year_nodes else None
    year = int(re.search(r'\d+', year_str).group()) if year_str else None

    # 获取类型
    genre_nodes = tree.xpath('//span[@property="v:genre"]')
    genre = ",".join([node.text.strip() for node in genre_nodes]) if genre_nodes else None

    # 获取地区
    area_nodes = tree.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[@class="pl"][contains(text(),"制片国家/地区")]/following-sibling::text()')
    area_str = area_nodes[0].strip() if area_nodes else None
    region = ','.join(area_str.split(' / ')) if area_str else None

    # 获取IMDb编号
    imdb_nodes = tree.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[@class="pl"][contains(text(),"IMDb")]/following-sibling::text()')
    imdb_id = imdb_nodes[0].strip() if imdb_nodes else None

    # 获取语言
    language_nodes = tree.xpath('//div[@class="subject clearfix"]/div[@id="info"]/span[@class="pl"][contains(text(),"语言:")]/following-sibling::text()')
    language = ','.join(language_nodes[0].split(' / ')) if language_nodes else None

    # 获取介绍
    desc_nodes = tree.xpath('//span[@property="v:summary"]')
    description = desc_nodes[0].text_content().strip().replace(' ', '').replace('\n', '') if desc_nodes else None

    # 获取评分
    score_nodes = tree.xpath('//div[@class="rating_self clearfix"]/strong[@class="ll rating_num"]/text()')
    score =  score_nodes[0].strip()  if score_nodes else None

    # 获取时长
    runtime_nodes = tree.xpath('//span[@property="v:runtime"]')
    r = runtime_nodes[0].text.strip() if runtime_nodes else None
    runtime = int(re.search(r'\d+', r).group()) if r else None

    if runtime is None:
        duration_nodes = tree.xpath('//span[@class="pl"][contains(text(),"单集片长")]/following-sibling::text()')
        duration_text = duration_nodes[0].strip() if duration_nodes else None
        runtime = int(re.search(r'\d+', duration_text).group()) if duration_text else None
    print(douban_id, name, region, year)
    return sqlmd.Movie(
        douban_id = douban_id,
        imdb_id = imdb_id,
        title = name,
        description = description,
        region = region,
        score = score,
        language = language,
        genre = genre,
        time = year,
        runtime=runtime
    )


async def process_data(movie_list, token):
    cn_stop_words = sw.stopwords()
    country, genre, year, rating, lan, word = {},{},{},{},{},{}
    duration = {
        '0-30': 0,
        '31-60': 0,
        '61-90': 0,
        '91-120': 0,
        '121-150': 0,
        '>150': 0,
    }
    for orm_movie in movie_list:
        # 地区
        if orm_movie['region']:
            for r in orm_movie['region'].split(','):
                if r in country:
                    country[r] += 1
                else: country[r] = 1
        # 类型
        if orm_movie['genre']:
            for g in orm_movie['genre'].split(','):
                if g in genre:
                    genre[g] += 1
                else:
                    genre[g] = 1
        # 年份
        if orm_movie['time']:
            y = orm_movie['time'][:3] + '0'
            if y in year:
                year[y] += 1
            else:
                year[y] = 1
        # 评分
        if orm_movie['score']:
            if orm_movie['score'] in rating:
                rating[orm_movie['score']] += 1
            else:
                rating[orm_movie['score']] = 1
        # 时长
        if orm_movie['runtime']:
            runtime = orm_movie['runtime']
            if runtime <= 30:
                duration['0-30'] += 1
            elif runtime <= 60:
                duration['31-60'] += 1
            elif runtime <= 90:
                duration['61-90'] += 1
            elif runtime <= 120:
                duration['91-120'] += 1
            elif runtime <= 150:
                duration['121-150'] += 1
            else:
                duration['>150'] += 1
        # 语言
        if orm_movie['language']:
            for l in orm_movie['language'].split(','):
                l = l.strip()
                if l in lan:
                    lan[l] += 1
                else:
                    lan[l] = 1
        # 字数
        if orm_movie['description']:
            ls = jieba.lcut(orm_movie['description'])
            for w in ls:
                if len(w) == 1 or w in string.punctuation or w in cn_stop_words:
                    continue
                if w in word:
                    word[w] += 1
                else:
                    word[w] = 1
    word = OrderedDict(sorted(word.items(), key=lambda item: item[1], reverse=True)[:50])
    new_moviestats = sqlmd.MovieStats(
        country=json.dumps(country),
        genre=json.dumps(genre),
        year=json.dumps(year),
        rating=json.dumps(rating),
        duration=json.dumps(duration),
        lan=json.dumps(lan),
        word=json.dumps(word)
    )
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())\
            .options(selectinload(sqlmd.StoreRecord.store))
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        session.add(new_moviestats)
        await session.flush()
        orm_record.store.m_id = new_moviestats.id
        await session.commit()