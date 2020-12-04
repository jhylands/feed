from database import session_scope, Entry


def get_items():
    with session_scope() as session:
        entries = [{"title":e.title, "link":e.link, "image":e.image} for e in session.query(Entry).all()]
    return entries
