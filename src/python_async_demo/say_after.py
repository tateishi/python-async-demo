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


def mainloop() -> None:
    asyncio.run(async_main())


def main() -> None:
    Fire(mainloop)
