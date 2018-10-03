# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup

import pprint

NEXT_RACE_INFO_URL = "http://pog-info.com/archives/category/pog/news"


class Soup:

    def __init__(self, target_url, parser, seconds):
        self.target_url = target_url
        self.parser = parser
        self.seconds = seconds

    def get(self):
        time.sleep(self.seconds)
        r = requests.get(self.target_url)
        if r.status_code == requests.codes.ok:
            return BeautifulSoup(r.content, self.parser)
        else:
            return None


def get_next_race_info_url():
    soup = Soup(NEXT_RACE_INFO_URL, "lxml", 1)
    html = soup.get()
    print(html.find("a").get("href"))


def main():
    get_next_race_info_url()


if __name__ == "__main__":
    main()
