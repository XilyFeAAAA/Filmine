import os
import random
import string
import smtplib
from email.message import EmailMessage
from configs import smtp
# Sql Related
from sql import models as sqlmd
from sql.engine import general as engine
# SQLAlchemy Related
from sqlalchemy import select, or_, false, true
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from models.exceptions import VerifyNotExist

async def send_verification_email(email: str):
    link = await generate_verification_link(email)
    
    msg = EmailMessage()
    msg.set_content(f'这是邮件正文,包含一个链接: <a href="{link}">点击访问</a>', subtype="html")
    msg["Subject"] = "Email Verification"
    msg["From"] = f"<{smtp.email}>"
    msg["To"] = f"<{email}>"

    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server.login(smtp.email, smtp.password)
        server.send_message(msg, smtp.email, email)



async def generate_verification_link(email: str, token_length=16):
    base_url = 'http://127.0.0.1:7070'
    # 生成随机令牌
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=token_length))
    new_verify = sqlmd.Verify(token=token, email=email)
    # link to SQL and add record
    async with AsyncSession(engine) as session:
        session.add(new_verify)
        await session.commit()
    # 构建验证链接
    verification_link = f"{base_url}/user/verify-account/{token}"
    return verification_link

async def is_valid_token(token: str):
    async with AsyncSession(engine) as session:
        stmt = select(sqlmd.Verify)\
                .filter(sqlmd.Verify.token == token)\
                .filter(sqlmd.Verify.deleted == false())
        try:
            orm_verify = (await session.execute(stmt)).scalar_one()
            orm_verify.state = True
            email = orm_verify.email
            await session.commit()
        except NoResultFound:
            raise VerifyNotExist()
    return email