#!/usr/bin/env python3
#
#   This is a tool for gathering image from the internet
#
import argparse
import errno
import os
import re
import urllib

from urllib.request import urlopen
from bs4 import BeautifulSoup, ResultSet


class Scrapper:
    def get_urls(self, search_url: str) -> ResultSet:
        """
        Scrap the website page and get the images URL

        :param search_url: Target website URL
        :type search_url: str

        :return: set of images URL
        :rtype: ResultSet
        """
        req = urllib.request.Request(search_url)
        with urllib.request.urlopen(req) as response:
            page = response.read()

        bs = BeautifulSoup(page, 'html.parser')
        re_files_format = ".svg|.jpg|.jpeg|.png|.gif"
        images_url = bs.find_all('img', {'src': re.compile(re_files_format)})
        print(f'{len(images_url)} images found!')
        return images_url

    def save_urls_to_file(self, images_url: ResultSet) -> bool:
        """
        Save the images URL to a txt file

        :param images_url: Set of images URL
        :type images_url: ResultSet

        :return: True if succeed
        :rtype: bool
        """
        # Creating directory and file if doesn't exists
        file_path = "../data/images_urls.txt"
        if not os.path.exists(os.path.dirname(file_path)):
            try:
                os.makedirs(os.path.dirname(file_path))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        # Saving content to txt file
        with open(file_path, "w") as f:
            for image in images_url:
                f.write("https:" + image['src'] + '\r\n')
        return True


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-u", "--url", dest="url", action="store", required=True,
                            help="URL of the website to download the images")

    arg_parser.add_argument("-d", "--download", dest="download", action="store_true",
                            help="Download flag, the images will be downloaded")

    args = arg_parser.parse_args()

    scrapper = Scrapper()
    images_url = scrapper.get_urls(args.url)
    scrapper.save_urls_to_file(images_url)
