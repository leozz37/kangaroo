import pytest

from scrap.scrapper import Scrapper
from scrap.scrapper import main


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


def test_format_urls_with_success(scrapper: Scrapper) -> None:
    """
    Test if the URL has has te correct format
    """
    url = "http://www.pudim.com.br"
    images_url = scrapper.get_urls(url)

    expected_output = "http://www.pudim.com.br/pudim.jpg"
    result = scrapper.format_urls(url, images_url)

    assert result[0] == expected_output


def test_format_urls_without_initial_url_with_success(scrapper: Scrapper) -> None:
    """
    Test if the URL has has te correct format
    """
    url = "https://pt.wikipedia.org/wiki/Brasil"
    images_url = scrapper.get_urls(url)

    expected_output = "http://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/" + \
                      "Cscr-featured1.png/20px-Cscr-featured1.png"
    result = scrapper.format_urls(url, images_url)

    assert result[0] == expected_output


def test_validate_url_with_success(scrapper: Scrapper) -> None:
    """
    Test if the URL is valid
    """
    url = "http://www.pudim.com.br"
    result = scrapper.validate_url(url)

    assert result is True


def test_validate_url_fails(scrapper: Scrapper) -> None:
    """
    Test if the URL is valid
    """
    url = "pudim.com.br"
    result = scrapper.validate_url(url)

    assert result is False


def test_save_urls_to_file_with_success(scrapper: Scrapper) -> None:
    """
    Test if URLs are being saved into txt
    """
    url = "http://www.pudim.com.br/"
    images_url = scrapper.get_urls(url)
    images_url = scrapper.format_urls(url, images_url)
    scrapper.save_urls_to_file(images_url)

    expected_output = images_url[0] + "\n"
    resulted_output = open("../data/images_urls.txt", "r").read()

    assert expected_output == resulted_output
