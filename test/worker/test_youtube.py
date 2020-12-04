
from database import session_scope
from worker.youtube import Youtube

def test_Youtube():
    entries = list(Youtube().get())
    with session_scope() as session:
        for entry in entries:
            session.add(entry)
        session.commit()
