# from official doc
import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def entrypoint_gather():
    # Schedule three calls *concurrently*:
    tasks = []

    for i in range(1, 4):
        tasks.append(asyncio.create_task(factorial(i, i + 1)))

    L = await asyncio.gather(*tasks)
    print(L)


async def entrypoint_taskgroup_without_results():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 4):
            tg.create_task(factorial(i, i + 1))


async def entrypoint_taskgroup():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i in range(1, 4):
            task = tg.create_task(factorial(i, i + 1))
            tasks.append(task)

    L = [task.result() for task in tasks]
    print(L)


def main(entrypoint=entrypoint_gather):
    asyncio.run(entrypoint())
