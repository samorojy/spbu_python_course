import asyncio
import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.thisfuckeduphomerdoesnotexist.com/"


def get_homer_image_url() -> str:
    html = urllib.request.urlopen(URL).read()
    image_url = BeautifulSoup(html, "html.parser").find(id="image-payload")["src"]
    return image_url


async def download_homer(path: str):
    homer_image = urllib.request.urlopen(get_homer_image_url())
    with open(path, "wb") as localFile:
        localFile.write(homer_image.read())


async def download_homers_async(amount: int, path: str = ""):
    tasks = [asyncio.create_task(download_homer(path + f"{i + 1}.jpg")) for i in range(0, amount)]
    for task in tasks:
        await task


asyncio.run(download_homers_async(3))
