from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select
from sqlalchemy.orm import selectinload


from sql import models as sqlmodels

import configs


# General engine for SQL connection to the backend database
general = create_async_engine(f"mysql+aiomysql://{configs.sql.username}:{configs.sql.password}@{configs.sql.host}:{configs.sql.ip}/{configs.sql.db_name}?charset={configs.sql.charset}")


# import asyncio
# from .models import Admin

# async def init_models():
#     async with general.begin() as conn:
#         await conn.run_sync(Admin.metadata.drop_all)
#         await conn.run_sync(Admin.metadata.create_all)

# asyncio.run(init_models())