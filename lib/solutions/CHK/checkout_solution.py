# noinspection PyUnusedLocal
# skus = unicode string

import re
from collections import Counter

PRICE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

SPECIAL_OFFERS = {
    "A": {"quantity": 3, "price": 130},
    "B": {"quantity": 2, "price": 45},
}


def is_valid_items(items: str) -> bool:
    letters_to_remove = "".join(list(PRICE.keys()))
    re_pattern = f"[{letters_to_remove}]"
    invalid_items = re.sub(re_pattern, "", items)

    return not bool(invalid_items)


def checkout(skus: str) -> int:
    items = skus.upper()
    if not is_valid_items(items):
        return -1


def calculate_item_price(item: str, count: int) -> int:
    discount = SPECIAL_OFFERS.get(item)
    if discount:
        apply_offer_quntity = count // discount["quantity"]
        discount_price = apply_offer_quntity * discount["price"]

        items_no_discount = count % discount["quantity"]
        non_discounted_price = items_no_discount * PRICE[item]
        return discount_price + non_discounted_price
    else:
        return count * PRICE[item]



def calculate(skus: str) -> int:
    items = skus.upper()

    if not is_valid_items(items):
        return -1

    total_price = 0
    sku_items = Counter(skus.upper())
    for item, count in sku_items.items():
        total_price += calculate_item_price(item, count)
       
    return total_price
    



