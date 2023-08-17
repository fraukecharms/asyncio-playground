# demo of unawaited vs awaited tasks
# examples from python standard library docs
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def entrypoint_without_await():
    # aka do not do this part 2
    task1 = asyncio.create_task(say_after(1, "hello"))  # noqa
    task2 = asyncio.create_task(say_after(2, "world"))  # noqa

    print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")


async def entrypoint_with_await():
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


def main(entrypoint=entrypoint_with_await):
    asyncio.run(entrypoint())
