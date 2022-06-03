import asyncio
import time

from fire import Fire


async def task_one():
    print("task_one: before sleep")
    await asyncio.sleep(10)
    print("task_one: after  sleep")
    return 1


async def time_sleep():
    time.sleep(5)
    print("time_sleep")


async def task_two():
    print("task_two: before task_one")
    await asyncio.sleep(1)
    print("task_two: after  task_one")
    return 2


async def test(loop):
    t1 = loop.create_task(task_one())
    t2 = loop.create_task(task_two())

    print(repr(await t1))
    print(repr(await t2))


def test_main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(test(loop))
    finally:
        loop.close()


def main():
    Fire(test_main)
