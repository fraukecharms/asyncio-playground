# adapted from https://lukasz.langa.pl/6d439b86-3834-481a-b95c-ac9c6956545b/
import asyncio

from termcolor import cprint


async def say_after(delay, id, color):
    try:
        cprint(f"started task {id}", color)
        await asyncio.sleep(delay)
        cprint(f"task {id}", color)
    finally:
        cprint(f"start cleaning up {id}", color)
        await asyncio.sleep(0.1)
        cprint(f"finish cleaning up {id}", color)


async def entrypoint_wait(delays, colors, timeout):
    tasks = []

    for task_id in range(len(delays)):
        tasks.append(asyncio.create_task(say_after(delays[task_id], str(task_id), colors[task_id])))

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.ALL_COMPLETED,
    )

    print("\nstarting cancellation\n")

    for task in pending:
        task.cancel()

    if pending:
        done, pending = await asyncio.wait(
            pending,
            return_when=asyncio.ALL_COMPLETED,
        )

    print(f"\nnumber of pending tasks: {len(pending)}")


async def entrypoint_taskgroup(delays, colors, timeout):
    tasks = []

    try:
        async with asyncio.timeout(timeout):
            async with asyncio.TaskGroup() as tg:
                for task_id in range(len(delays)):
                    task = tg.create_task(say_after(delays[task_id], str(task_id), colors[task_id]))
                    tasks.append(task)
    except TimeoutError:
        print("timeout")


def main(entrypoint=entrypoint_wait, timeout=1):
    delays = [1.4, 1.5, 1.9]
    colors = ["red", "green", "blue"]
    # try timeout 5 and 1
    print(f"timeout set to {timeout} seconds")
    asyncio.run(entrypoint(delays, colors, timeout))
