import asyncio
import time

from fire import Fire


async def hello_world(n):
    await asyncio.sleep(2)
    print(f"{n}: hello world")


async def call_hello_world1():
    print("call_hello_world1()")
    await hello_world(1)


async def call_hello_world2():
    print("call_hello_world2()")
    await hello_world(2)


def async_loop():
    loop = asyncio.get_event_loop()
    loop.create_task(call_hello_world1())
    loop.run_until_complete(call_hello_world2())


def main():
    Fire(async_loop)
