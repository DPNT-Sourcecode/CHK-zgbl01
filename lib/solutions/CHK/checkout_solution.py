# noinspection PyUnusedLocal
# skus = unicode string

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
    valid_items = str(PRICE.keys())
    invalid_items = items.replace(valid_items, "")
    return bool(invalid_items)


def checkout(skus: str) -> int:
    items = skus.upper()

    if not is_valid_items(items):
        return -1

    sku_items = Counter(skus.upper())

    total_price = 0
    for item, count in sku_items.items():

        discounts = SPECIAL_OFFERS.get(item)
        if discounts:
            apply_offer_quntity = count // discounts["quantity"]
            discount_price = apply_offer_quntity * discounts["price"]

            items_no_discount = count % discounts["quantity"]
            non_discounted_price = items_no_discount * PRICE.get(item, 0)
            total_price += discount_price + non_discounted_price
        else:
            try:
                item_price = PRICE[item]
            except IndexError:
                return -1

            total_price += count * item_price       

    return total_price
    

