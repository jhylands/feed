from app.item_manager import get_items


def test_get_items():
    items = get_items()
    for item in items:
        print(item.title)
