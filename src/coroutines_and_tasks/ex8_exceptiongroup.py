# adapted from https://github.com/jrfk/talk/tree/main/EuroPython2023
# and https://lukasz.langa.pl/6d439b86-3834-481a-b95c-ac9c6956545b/

import asyncio


async def coro_success():
    await asyncio.sleep(0.5)
    print("running")
    return "success"


async def coro_value_err():
    raise ValueError("some value error")


async def coro_type_err():
    raise TypeError("some type error")


async def entrypoint_exceptiongroup():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(coro_value_err())
            task2 = tg.create_task(coro_type_err())
            task3 = tg.create_task(coro_success())

        results = [task1.result(), task2.result(), task3.result()]  # noqa
    except BaseExceptionGroup as eg:
        print(eg.exceptions)


async def entrypoint_except_star():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(coro_value_err())
            task2 = tg.create_task(coro_type_err())
            task3 = tg.create_task(coro_success())
            task4 = tg.create_task(coro_type_err())

        results = [task1.result(), task2.result(), task3.result(), task4.result()]  # noqa
    except* ValueError as ve_group:
        print(ve_group.exceptions)
    except* TypeError as te_group:
        print(te_group.exceptions)


def main(entrypoint=entrypoint_except_star):
    asyncio.run(entrypoint())
