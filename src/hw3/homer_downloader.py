import asyncio

import aiohttp
from bs4 import BeautifulSoup

URL = "https://www.thisfuckeduphomerdoesnotexist.com/"


async def get_homer_image_url(session: aiohttp.ClientSession) -> str:
    async with session.get(URL) as response:
        html = await response.read()
        image_url = BeautifulSoup(html, "html.parser").find(id="image-payload")["src"]
        return image_url


async def download_homer(session: aiohttp.ClientSession, path: str):
    homer_url = await get_homer_image_url(session)
    async with session.get(homer_url) as response:
        with open(path, "wb") as localFile:
            localFile.write(await response.read())


async def download_homers_async(amount: int, path: str = ""):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_homer(session, path + f"{i + 1}.jpg")) for i in range(0, amount)]
        await asyncio.gather(*tasks)


def user_interface():
    print("Enter the number of inclusive homers you want to download:")
    homers_amount = input()
    while type(homers_amount) != int:
        try:
            homers_amount = int(homers_amount)
        except ValueError:
            print("Enter int number of inclusive homers you want to download:")
            homers_amount = input()
    asyncio.get_event_loop().run_until_complete(download_homers_async(homers_amount))
    print(f"{homers_amount} homers uploaded successfully")
