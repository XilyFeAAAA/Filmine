# Fundamental
from typing import Tuple
from time import time
# SQLAlchemy Related
from sqlalchemy import select, or_, false, true
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

# Core Related
from core.security import verify_password, get_password_hash
from core.utils import send_verification_email
# Sql Related
from sql import models as sqlmd
from sql.engine import general as engine

# Model Related
from models.user import SafeUserModel, NewUserModel
from models.exceptions import UserNotExist, IncorrectPassword, UserAlreadyExist, NotVerified

async def login(username: str, password: str) -> SafeUserModel:
    '''General Depends function for user authetication

    If success, return userInfo, else return the LoginResult with err_msg'''
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.User)\
                .filter(sqlmd.User.username == username)\
                .filter(sqlmd.User.deleted == false())
        try:
            orm_user = (await session.execute(stmt)).scalar_one()
            hashed_pwd = orm_user.hashed_password
        except NoResultFound:
            raise UserNotExist()
        if verify_password(password, hashed_pwd):
            if not orm_user.verified:
                raise NotVerified()
            return SafeUserModel(**orm_user.__dict__)
        else:
            raise IncorrectPassword()


async def register(new_user_info: NewUserModel) -> None:
    '''Create a new user, add the user info into SQL database'''
    bpassword = new_user_info.password
    # hash the password
    hashed_password = get_password_hash(bpassword)

    # create a ORM User class instance of this new user
    new_user = sqlmd.User(
        username=new_user_info.username,
        email=new_user_info.email,
        hashed_password=hashed_password,
        created_time=int(round(time() * 1000))
    )
    stmt = select(sqlmd.User)\
            .filter(or_(sqlmd.User.username == new_user_info.username,
                        sqlmd.User.email == new_user_info.email))\
            .filter(sqlmd.User.deleted == false())
    # link to SQL and add record
    async with AsyncSession(engine) as session:
        # check if already has user with same email or username
        res = await session.execute(stmt)
        count = len(res.fetchall())
        # if already has user, raise error
        if count > 0:
            raise UserAlreadyExist()
        session.add(new_user)
        await session.commit()
    await send_verification_email(new_user_info.email)

async def delete(username: str) -> None:
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.User)\
                .filter(sqlmd.User.username == username)\
                .filter(sqlmd.User.deleted == false())
        try:
            orm_user = (await session.execute(stmt)).scalar_one()
            orm_user.deleted = True
            await session.commit()
        except NoResultFound:
            raise UserNotExist()
        
async def verify_user(email: str):
     async with AsyncSession(engine) as session:
        stmt = select(sqlmd.User)\
                .filter(sqlmd.User.email == email)\
                .filter(sqlmd.User.deleted == false())
        try:
            orm_user = (await session.execute(stmt)).scalar_one()
            orm_user.verified = True
            await session.commit()
        except NoResultFound:
            raise UserNotExist()