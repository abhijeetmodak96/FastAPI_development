# python types usage examples:
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items1(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items2(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item(item: int | str):
    print(item)


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


print(get_full_name("john", "doe"))
