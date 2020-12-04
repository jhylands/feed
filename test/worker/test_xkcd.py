from worker.xkcd import XKCD
from bs4 import BeautifulSoup as BS

def test_XKCD():
    entries = list(XKCD().get())
    assert entries[0].title!=""

def test_get_image():
    assert BS("""<summary type="html"><img src="https://imgs.xkcd.com/comics/cyber_cafe.png" title="Since we haven't really settled on a name for those online hangout/work spaces that try to recreate the experience of cafes, and I love confusion, I'm going to start calling them 'cyber cafes' or 'internet cafes.'" alt="Since we haven't really settled on a name for those online hangout/work spaces that try to recreate the experience of cafes, and I love confusion, I'm going to start calling them 'cyber cafes' or 'internet cafes.'" /></summary>""").summary.img['src'] == "https://imgs.xkcd.com/comics/cyber_cafe.png"
