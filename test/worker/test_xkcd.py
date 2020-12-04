from database import session_scope
from worker.xkcd import XKCD
from bs4 import BeautifulSoup as BS

def test_XKCD():
    entries = list(XKCD().get())
    with session_scope() as session:
        for entry in entries:
            session.add(entry)
        session.commit()
