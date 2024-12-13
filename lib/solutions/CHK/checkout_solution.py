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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

DISCOUNTS = {
    "A": {5: 200, 3: 130},
    "B": {2: 45},
    "H": {10: 80, 5: 45},
    "K": {2: 120},
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


def check_group_discount(items: str) -> tuple[int, str]:
    """
    Evaluatesand returns how many multiples of STXYZ are presents in the
    items and as well as the remaining string of items
    """

    remaining_items = Counter(items)
    group_discount_items = {}
    for item in "ZYSTX":
        if remaining_items[item] > 0:
            group_discount_items[item] = remaining_items[item]
            del remaining_items[item]

    group_multiples = sum(group_discount_items.values()) // 3

    # Need to go through the odd items that group discount does not apply
    # and put them back into remaining_items, so that they can be
    # charged a normal price
    group_remainders = sum(group_discount_items.values()) % 3
    for _ in range(group_remainders):
        # Work backwards with the last key, because we want to
        # charge for the cheapest items.
        last_key = list(group_discount_items.keys())[-1]

        item_count = remaining_items.get(last_key, 0)
        remaining_items[last_key] = item_count + 1

        # If the count reaches zero, we need to remove them
        # from the group_discount_items, so that we can start
        # charging for the 2nd cheapest items, etc.
        group_discount_items[last_key] -= 1
        if group_discount_items[last_key] == 0:
            del group_discount_items[last_key]

    remaining_item_str = "".join(
        item * count for item, count in remaining_items.items()
    )

    return group_multiples, remaining_item_str


def checkout(skus: str) -> int:
    """
    Returns the total amount for the given SKUs.
    """
    if not is_valid_items(skus):
        return -1

    total_price = 0

    free_items = {}
    for item, count in Counter(skus).items():
        free_items_offer = FREE_ITEMS.get(item)
        if free_items_offer is not None:
            get_free_items(item, count, free_items_offer, free_items)

    group_discount_multiplier, remaining_items = check_group_discount(skus)
    total_price += group_discount_multiplier * 45

    for item, count in Counter(remaining_items).items():
        price = calculate_item_price(item, count, free_items)
        total_price += price

    return total_price

