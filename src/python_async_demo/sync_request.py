# https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp-jp

import time

import requests
from fire import Fire


def sync_request():
    start_time = time.time()

    for number in range(1, 151):
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon["name"])

    print(f"--- {time.time() - start_time} seconds ---")


def main():
    Fire(sync_request)
