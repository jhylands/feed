from bs4 import BeautifulSoup as BS
from database import Entry
import requests


class UnimpementedExcepiton(Exception):
    pass


class Feed:
    def get(self):
        result = requests.get(self.url)
        xml = BS(result.text, features="lxml")
        for entry in self.get_entries(xml):
            yield Entry(
                title=self.get_title(entry),
                image=self.get_image(entry),
                link=self.get_link(entry))

    # Abstract functions to be overwritten
    def get_title(entity):
        raise UnimpementedExcepiton("get_title")

    def get_image(entity):
        raise UnimpementedExcepiton("get_image")

    def get_link(entity):
        raise UnimpementedExcepiton("get_link")
