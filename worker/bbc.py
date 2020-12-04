
from worker.feed import Feed


class BBC(Feed):
    def __init__(self):
        self.url = "http://feeds.bbci.co.uk/news/rss.xml"

    @staticmethod
    def get_entries(xml):
        return xml.find_all("item")

    @staticmethod
    def get_title(entry):
        return entry.title.text

    @staticmethod
    def get_image(entry):
        return ""

    @staticmethod
    def get_link(entry):
        return entry.link.text
