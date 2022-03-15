import asyncio
import os
import tempfile

from src.hw3.task2.homer_downloader import get_homer_image_url, download_homer


def test_get_homer_image_url():
    homer_image = get_homer_image_url()
    assert type(homer_image) == str


def test_download_homer():
    temp_dir = tempfile.mkdtemp()
    asyncio.run(download_homer(temp_dir + "/1.jpg"))
    assert len(os.listdir(temp_dir)) != 0
