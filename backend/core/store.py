# Fundamental
import asyncio
import json
import secrets
from typing import List, Tuple
from time import time
# SQLAlchemy Related
from sqlalchemy import select, or_, false, true
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

# Sql Related
from sql import models as sqlmd
from sql.engine import general as engine

# Model Related
from models.store import StoreModel,StoreRecordModel
from models.exceptions import RecordNotExist,UserAlreadyExist,MovieNotExist,MovieStatsNotExist

async def add(user_name: str) -> str:
    async with AsyncSession(engine) as session: 
        stmt = select(sqlmd.User)\
                .filter(sqlmd.User.username == user_name)\
                .filter(sqlmd.User.deleted == false())
        orm_user = (await session.execute(stmt)).scalar_one_or_none()
        if orm_user is None:
            raise UserAlreadyExist()
        user_id = orm_user.id
    token = secrets.token_hex(8)[:16]
    new_record = sqlmd.StoreRecord(
        u_id=user_id,
        token=token,
        created_time=int(round(time() * 1000)))
    async with AsyncSession(engine) as session:
        session.add(new_record)
        await session.commit()
    return token

async def get(user_name: str) -> List[StoreRecordModel]:
    async with AsyncSession(engine) as session: 
        stmt = select(sqlmd.User)\
                .filter(sqlmd.User.username == user_name)\
                .filter(sqlmd.User.deleted == false())\
                .options(selectinload(sqlmd.User.store_record))
        orm_user = (await session.execute(stmt)).scalar_one_or_none()
        if orm_user is None:
            raise UserAlreadyExist()
        records = [StoreRecordModel(**record.__dict__) for record in orm_user.store_record if record.completed]
    return records

async def project(token: str) -> StoreModel:
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())\
            .options(selectinload(sqlmd.StoreRecord.store))
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        store = StoreModel(**orm_record.store.__dict__)
    return store 

async def deploy(new_deploy_info: StoreModel, token: str):
    new_store = sqlmd.Store(
        name=new_deploy_info.name,
        source=new_deploy_info.source,
        notes=new_deploy_info.notes,
        cookie=new_deploy_info.cookie,
        email=new_deploy_info.email,
        created_time=int(round(time() * 1000))
    )
    stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        session.add(new_store)
        await session.flush()
        orm_record.s_id = new_store.id
        await session.commit()
    return true


async def getQrcode(token: str):
    stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())\
            .options(selectinload(sqlmd.StoreRecord.crawl))
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        # 验证码还未刷新
        if orm_record.crawl is None:
            return False
        url = orm_record.crawl.qrcode_url
    return url


async def getState(token: str):
    stmt = select(sqlmd.StoreRecord)\
       .filter(sqlmd.StoreRecord.token == token)\
       .filter(sqlmd.StoreRecord.deleted == false())\
       .options(selectinload(sqlmd.StoreRecord.crawl))
    async with AsyncSession(engine) as session:
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        # 验证码还未刷新
        if orm_record.crawl is None:
            return False
        state = orm_record.crawl.running
    return state


async def getMovieStats(token: str):
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.StoreRecord)\
            .filter(sqlmd.StoreRecord.token == token)\
            .filter(sqlmd.StoreRecord.deleted == false())\
            .options(selectinload(sqlmd.StoreRecord.store)\
                     .selectinload(sqlmd.Store.moviestats))
        orm_record = (await session.execute(stmt)).scalar_one_or_none()
        if orm_record is None:
            raise RecordNotExist()
        print()
        if orm_record.store.moviestats is None:
            raise MovieStatsNotExist()
        orm_moviestats = orm_record.store.moviestats
    # 国家
    return {
        "country": json.loads(orm_moviestats.country),
        "genre": json.loads(orm_moviestats.genre),
        "year": json.loads(orm_moviestats.year),
        "rating": json.loads(orm_moviestats.rating),
        "duration": json.loads(orm_moviestats.duration),
        "lan": json.loads(orm_moviestats.lan),
        "word": json.loads(orm_moviestats.word)
    }



