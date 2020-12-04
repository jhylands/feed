from bs4 import BeautifulSoup as BS
from worker.feed import Feed
import html


class XKCD(Feed):
    def __init__(self):
        self.url = "https://xkcd.com/atom.xml"

    @staticmethod
    def get_entries(xml):
        return xml.find_all("entry")

    @staticmethod
    def get_title(entry):
        return entry.title.text

    @staticmethod
    def get_image(entry):
        return BS(html.unescape(entry.summary.text)).img['src']

    @staticmethod
    def get_link(entry):
        return entry.link["href"]
