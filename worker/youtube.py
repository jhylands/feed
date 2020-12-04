from worker.feed import Feed


class Youtube(Feed):
    def __init__(self):
        self.url = "https://www.youtube.com/feeds/videos.xml?channel_id=UCZFipeZtQM5CKUjx6grh54g"

    @staticmethod
    def get_entries(xml):
        return xml.find_all("entry")

    @staticmethod
    def get_title(entry):
        return entry.title.text

    @staticmethod
    def get_image(entry):
        return entry.find_all("media:thumbnail")[0]["url"]

    @staticmethod
    def get_link(entry):
        return entry.link["href"]
