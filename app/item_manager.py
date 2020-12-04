from database import session_scope, Entry


def get_items():
    with session_scope() as session:
        entries = [e.entry for e in session.query(Entry).all()]
    return entries
