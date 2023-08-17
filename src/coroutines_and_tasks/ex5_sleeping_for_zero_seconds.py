import asyncio
import time


async def coro_my_turn():
    time.sleep(0.5)
    print("my turn")


async def coro_long():
    time.sleep(0.5)
    a = 45 * 13
    print(a)
    time.sleep(1)
    b = 98 - 9
    print(b)


async def coro_long_with_asyncio_sleep():
    time.sleep(0.5)
    a = 45 * 13
    print(a)
    await asyncio.sleep(0)
    time.sleep(1)
    b = 98 - 9
    print(b)


async def entrypoint_uninterrupted():
    async with asyncio.TaskGroup() as tg:
        task2 = tg.create_task(coro_long())  # noqa
        task3 = tg.create_task(coro_my_turn())  # noqa


async def entrypoint_zero_sleep():
    async with asyncio.TaskGroup() as tg:
        task2 = tg.create_task(coro_long_with_asyncio_sleep())  # noqa
        task3 = tg.create_task(coro_my_turn())  # noqa


def main(entrypoint=entrypoint_uninterrupted):
    asyncio.run(entrypoint())
