# -*- coding: utf-8 -*-

import time

import requests
from bs4 import BeautifulSoup

import pprint

NEXT_RACE_INFO_URL = "http://pog-info.com/archives/category/pog/news"
NEXT_RACE_ARTICLE_URL = "http://pog-info.com/archives/{}"


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


def get_next_race_info_id():
    soup = Soup(NEXT_RACE_INFO_URL, "lxml", 1)
    html = soup.get()
    return html.find("article").get("id").split("-")[1]


def get_next_race_info(article_id):
    soup = Soup(NEXT_RACE_ARTICLE_URL.format(article_id), "lxml", 1)
    next_race_content = soup.get().find("div", class_="single-entry-content")
    return next_race_content


def main():
    pass


if __name__ == "__main__":
    main()
