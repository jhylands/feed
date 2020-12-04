from database import session_scope, Entries


def get_items():
    with session_scope() as session:
        session.add(Entries(entry="1"))
        session.commit()
        entries = [e.entry for e in session.query(Entries).all()]
    return entries
