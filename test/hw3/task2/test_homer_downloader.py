from src.hw3.task2.homer_downloader import get_homer_image_url


def test_get_homer_image_url():
    homer_image = get_homer_image_url()
    assert type(homer_image) == str
