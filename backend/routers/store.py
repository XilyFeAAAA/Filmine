# Fundamental
import asyncio
import threading
import multiprocessing
from fastapi import APIRouter, BackgroundTasks, Depends, Body, Request
from fastapi.security import OAuth2PasswordRequestForm

# Core Related
from core import store as coreStore
from core.crawl import run_sync_main
from core.security import authenticate_admin, generate_token

# Models Related
from models.store import StoreModel, DoubanModel
from models.response import Response400, ResponseToken,Response200

router = APIRouter()

@router.get('/add', response_model=Response200 | Response400)
async def add(request: Request, payload: dict = Depends(authenticate_admin)) -> Response200 | Response400:
    '''仓库路由 - 注册事件'''
    try:
        token = await coreStore.add(payload['username'])
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200(data={'token': token})



@router.post('/deploy', response_model=Response200 | Response400)
async def deploy(request: Request, new_deploy_info: StoreModel = Body(), token: str = Body(),
                 payload: dict = Depends(authenticate_admin)) -> Response200 | Response400:
    '''仓库路由 - 部署事件'''
    try:
        await coreStore.deploy(new_deploy_info, token)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    # 开启爬虫线程
    print("开始后台任务")
    # 线程和进程到时候在看
    multiprocessing.Process(target=run_sync_main, args=(token,)).start()
    # threading.Thread(target=run_sync_main, args=(token,)).start()
    print('线程开启，返回200')
    return Response200(data={"message": "Crawling movies in background..."})

@router.get('/qrcode/{token}', response_model=Response200 | Response400)
async def qrcode(request: Request, token: str, payload: dict = Depends(authenticate_admin)):
    '''仓库路由 - 获取二维码'''
    # 返回二维码
    try:
        res = await coreStore.getQrcode(token)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    # 还未加载
    if not res:
        return Response400(err_msg="验证码还未加载,请稍后")
    return Response200(data={'url': res})
    
@router.get('/state/{token}', response_model=Response200 | Response400)
async def qrcode(request: Request, token: str, payload: dict = Depends(authenticate_admin)):
    '''仓库路由 - 获取二维码'''
    # 返回状态
    try:
        res = await coreStore.getState(token)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200(data={'progress': res})
    
@router.get('/get', response_model=Response200 | Response400)
async def get(request: Request, payload: dict = Depends(authenticate_admin)):
    try:
        info = await coreStore.get(payload['username'])
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200(data={'storeInfo': info})


@router.get('/project/{token}', response_model=Response200 | Response400)
async def project(request: Request, token: str, payload: dict = Depends(authenticate_admin)):
    '''仓库路由 - 获取项目具体信息'''
    # try:
    project = await coreStore.project(token)
    # except Exception as e:
        # return Response400(err_msg=e.__class__.__name__)
    return Response200(data={'project': project})

@router.get('/getMovieStats/{token}', response_model=Response200 | Response400)
async def getMovieStats(request: Request, token: str, payload: dict = Depends(authenticate_admin)):
    '''仓库路由 - 获取项目可视化信息'''
    try:
        res = await coreStore.getMovieStats(token)
    except Exception as e:
        return Response400(err_msg=e.__class__.__name__)
    return Response200(data={'stats': res})