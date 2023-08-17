# example from standard library docs
import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def entrypoint():
    print("In the entrypoint coroutine.")
    await say_after(1, "hello")


def main():
    asyncio.run(entrypoint())


# def main_crash():
#     await entrypoint()
#
