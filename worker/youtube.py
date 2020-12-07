from worker.feed import Feed


class Youtube(Feed):
    def __init__(self, channel_id):
        self.url = "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id

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

IssacArther = "UCZFipeZtQM5CKUjx6grh54g"
RobertMiles = "UCLB7AzTwc6VFZrBsO2ucBMg"
UpAndAtom = "UCSIvk78tK2TiviLQn4fSHaw"
SabineHossenfelder = "UC1yNl2E66ZzKApQdRuTQ4tw"
vsauce = "UC6nSFpj9HTCZ5t-N3Rm3-HA"
theCodingTrain = "UCvjgXvBlbQiydffZU7m1_aw"
Integza = "UC2avWDLN1EI3r1RZ_dlSxCw"

"""
Computerphile
Numberphile
Numberphile2
"""
