import asyncio
import time

from fire import Fire


async def say_after(delay: float, what: str) -> None:
    await asyncio.sleep(delay)
    print(f"{what} at {time.strftime('%X')}")


async def async_main() -> None:
    print(f"started at {time.strftime('%X')}")

    await say_after(1, "hello")
    await say_after(2, "world")

    print(f"finished at {time.strftime('%X')}")


def mainloop1() -> None:
    asyncio.run(async_main())


def main1() -> None:
    Fire(mainloop1)


async def tasks_main() -> None:
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


def mainloop2() -> None:
    asyncio.run(tasks_main())


def main2() -> None:
    Fire(mainloop2)
