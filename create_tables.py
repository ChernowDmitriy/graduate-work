import asyncio

from main import create_table


async def main():
    await create_table()

asyncio.run(main())
