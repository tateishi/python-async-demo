import asyncio
import sys
import time

import aiohttp
from fire import Fire

start_time = time.time()


async def async_aiohttp():
    async with aiohttp.ClientSession(trust_env=True) as session:
        pokemon_url = "https://pokeapi.co/api/v2/pokemon/151"
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon["name"])


def async_main():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_aiohttp())
    print(f"--- {time.time() - start_time} seconds ---")


def main1():
    Fire(async_main)
