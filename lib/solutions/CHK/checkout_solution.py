# noinspection PyUnusedLocal
# skus = unicode string

import re
from collections import Counter

PRICE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

DISCOUNTS = {
    "A": {5: 200, 3: 130},
    "B": {2: 45},
}

FREE_ITEMS = {
    "E": {"items_needed": 2, "item": "B"},
}


def calculate_free_items(count: int, free_item_allowance: dict[str, int]) -> None:
    free_item_allowance["item"] = count // free_item_allowance["items_needed"]


def is_valid_items(items: str) -> bool:
    """
    Returns a boolean indicating if the input items
    contains illegal items.
    """

    letters_to_remove = "".join(list(PRICE.keys()))
    re_pattern = f"[{letters_to_remove}]"
    invalid_items = re.sub(re_pattern, "", items)

    return not bool(invalid_items)


def calculate_discounted_price(item: str, count: int, discount: dict[str, int], free_item_allowance: dict[str, int]) -> int:
    """
    Returns the total amount for a
    given item with an applied discount
    """

    total_price = 0
    remaining_items = int(count)

    items_for_free = free_item_allowance.get(item, 0)
    remaining_items -= items_for_free

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
    discounts = DISCOUNTS.get(item)
    free_item_allowance = FREE_ITEMS.get(item)
    
    if free_items is not None:
        # We ignore the freebies as they do not impact the total price
        calculate_free_items(count, free_item_allowance)

    if discounts is not None:
        return calculate_discounted_price(item, count, discounts, free_items)
   

    return count * PRICE[item]


def checkout(skus: str) -> int:
    """
    Returns the total amount for the given SKUs.
    """
    if not is_valid_items(skus):
        return -1

    free_items = {}

    total_price = 0
    sku_items = Counter(skus)
    for item, count in sku_items.items():
        total_price += calculate_item_price(item, count, free_items)

    return total_price
