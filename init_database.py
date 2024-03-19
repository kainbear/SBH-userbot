import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

from database.orm import AsyncORM
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())



async def main():
    await AsyncORM.create_tables()


asyncio.run(main())