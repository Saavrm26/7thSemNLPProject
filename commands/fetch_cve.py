import asyncio
import httpx
from config import API_KEY, URL
import json

HEADERS = {"apiKey": API_KEY}
PAGE_SIZE = 2000
PARALLEL_REQ = 5


async def fetch_data(req_id):
    make_request = True
    start_index = req_id * PAGE_SIZE
    increment = PARALLEL_REQ * PAGE_SIZE
    async with httpx.AsyncClient(headers=HEADERS) as client:
        while make_request:
            url = f"{URL}?startIndex={start_index}"
            response = await client.get(url)
            json = response.json()
            start_index += increment
            if json["resultsPerPage"] == 0:
                make_request = False
            else:
                yield json


def save_json(file_name, json_data):
    with open(file_name, "w") as f:
        json.dump(json_data, f, indent=4)


async def fetch_cve():
    tasks = [asyncio.create_task(process_fetch_data(i)) for i in range(PARALLEL_REQ)]
    await asyncio.gather(*tasks)


async def process_fetch_data(i):
    async for result in fetch_data(i):
        file_name = f"artifacts/api_calls/result_{i}_{id(result)}.json"
        save_json(file_name, result)