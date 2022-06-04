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


async def async_requests_main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        for number in range(1, 151):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon["name"])


def async_main2():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_requests_main())
    print(f"--- {time.time() - start_time} seconds ---")


def main2():
    Fire(async_main2)


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return pokemon["name"]


async def async_gather_tasks():
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        for number in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{number}"
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))
        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


def async_main3():
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_gather_tasks())
    print(f"--- {time.time() - start_time} seconds ---")


def main3():
    Fire(async_main3)
