# noinspection PyUnusedLocal
# skus = unicode string

import re
from typing import Union
from collections import Counter

PRICE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}

DISCOUNTS = {
    "A": {5: 200, 3: 130},
    "B": {2: 45},
    "H": {10: 80, 5: 45},
    "K": {2: 150},
    "P": {5: 200},
    "Q": {3: 80},
    "V": {3: 130, 2: 90},
}

FREE_ITEMS = {
    "E": {"items_needed": 2, "item": "B"},
    "F": {"items_needed": 2, "item": "F"},
    "N": {"items_needed": 3, "item": "M"},
    "R": {"items_needed": 3, "item": "Q"},
    "U": {"items_needed": 3, "item": "U"},
}


def get_free_items(
    item: str,
    count: int,
    free_item_offer: dict[str, Union[str, int]],
    free_items: dict[str, int],
) -> None:
    """
    Updates free_items to specifyhow many items
    in the basket should be for free
    """
    if free_item_offer["item"] == item:
        # Buy n of X, get an additional X for free
        free_items[free_item_offer["item"]] = count // (
            free_item_offer["items_needed"] + 1
        )
    else:
        # Buy n of X, get Y for free
        free_items[free_item_offer["item"]] = count // free_item_offer["items_needed"]


def is_valid_items(items: str) -> bool:
    """
    Returns a boolean indicating if the input items
    contains illegal items.
    """

    letters_to_remove = "".join(list(PRICE.keys()))
    re_pattern = f"[{letters_to_remove}]"
    invalid_items = re.sub(re_pattern, "", items)

    return not bool(invalid_items)


def calculate_discounted_price(
    item: str, count: int, discount: dict[str, int], free_item_allowance: dict[str, int]
) -> int:
    """
    Returns the total amount for a
    given item with an applied discount
    """

    total_price = 0
    remaining_items = int(count)

    for quantity_needed, offer in discount.items():
        offer_quantity = remaining_items // quantity_needed
        if offer_quantity > 0:
            total_price += offer_quantity * offer
            remaining_items -= quantity_needed * offer_quantity

    non_discounted_price = remaining_items * PRICE[item]
    return total_price + non_discounted_price


def calculate_item_price(item: str, count: int, free_items: dict[str, int]) -> int:
    """
    Returns the total amount based on the input
    item and the number of items needed
    """
    remaining_items = int(count)

    free_item = free_items.get(item)
    if free_item is not None and item:
        remaining_items -= free_item

    discounts = DISCOUNTS.get(item)
    if discounts is not None:
        return calculate_discounted_price(item, remaining_items, discounts, free_items)

    return remaining_items * PRICE[item]


def check_group_discount(items: str) -> int:
    group_discount_items = re.sub(r"[STXYZ]", "", items)
    print()


def checkout(skus: str) -> int:
    """
    Returns the total amount for the given SKUs.
    """
    if not is_valid_items(skus):
        return -1

    """
    My Debugger keeps hanging and crashing...
    I keep stopping the exericse and the video as I keep restarting
    VS Code :(
    """

    total_price = 0
    sku_items = Counter(skus)
    
    check_group_discount(skus)

    free_items = {}
    for item, count in sku_items.items():
        free_items_offer = FREE_ITEMS.get(item)
        if free_items_offer is not None:
            get_free_items(item, count, free_items_offer, free_items)


    for item, count in sku_items.items():
        total_price += calculate_item_price(item, count, free_items)

    return total_price


