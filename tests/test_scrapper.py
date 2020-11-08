import pytest

from scrap.scrapper import Scrapper


@pytest.fixture
def scrapper() -> Scrapper:
    """
    Create an instance to be used across the test suite
    """
    # Set up
    scrapper = Scrapper()
    yield scrapper


def test_get_urls_with_success(scrapper: Scrapper) -> None:
    """
    Test if the size of the set of images is correct
    """
    url = "https://en.wikipedia.org/wiki/Albert_Einstein"
    images_url = scrapper.get_urls(url)

    # This value may vary in the future
    assert len(images_url) == 52


def test_get_urls_zero_images_with_success(scrapper: Scrapper) -> None:
    """
    Test if the size of the set of images is correct
    """
    # If you're wondering, yes I used random Wikipedia article
    url = "https://elliotjaystocks.com/"
    images_url = scrapper.get_urls(url)

    # This value may vary in the future
    assert len(images_url) == 0


def test_get_urls_one_image_with_success(scrapper: Scrapper) -> None:
    """
    Test if the size of the set of images is correct
    """
    url = "http://www.pudim.com.br/"
    images_url = scrapper.get_urls(url)

    # This value may vary in the future
    assert len(images_url) == 1
