# example from standard library docs
import asyncio
from datetime import datetime


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def entrypoint():
    start = datetime.now()

    for i in range(1, 4):
        await say_after(i, i)

    duration = datetime.now() - start
    print(f"Took {duration.total_seconds():.2f} seconds.")


def main():
    asyncio.run(entrypoint())
