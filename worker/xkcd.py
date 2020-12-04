from database import Entry
import requests
from bs4 import BeautifulSoup as BS


class XKCD:
    def get(self):
        result = requests.get("https://xkcd.com/atom.xml")
        xml = BS(result.text)
        for entry in xml.findall("entry"):
            yield Entry(
                title=entry.title.text,
                image=entry.summary.img.src,
                link=entry.link.href)
