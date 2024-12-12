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




def checkout(skus: str):
    sku_items = Counter(skus.upper())

    for item, count in sku_items.items():
        discounts = SPECIAL_OFFERS.get(item)
        if discounts:
            apply_offer_quntity = count // discounts["quantity"]
        else:
            apply_offer_quntity = 0
            print()



    print(items)
    




