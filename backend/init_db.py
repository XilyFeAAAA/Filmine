import asyncio
from sql.models import User
from sql.engine import general

async def init_models():
    async with general.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)
        await conn.run_sync(User.metadata.create_all)
      
asyncio.run(init_models())