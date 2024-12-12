import pytest

from lib.solutions.CHK.checkout_solution import checkout


"""
In production codebase, I would also mock PRICE and SPECIAL_OFFERS config, so that
the tests are not dependent on the config.  
"""


@pytest.mark.parametrize(
    "skus,expected_amount",
    [
        ("A", 50),
        ("A" * 3, 130),
        ("A" * 5, 200),
        ("A" * 6, 250),
        ("A" * 8, 330),
        ("A" * 10, 400),
        ("A" * 14, 580),
        ("A" * 15, 600),
    ],
)
def test_checkout_item_A(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount",
    [("B" * 1, 30), ("B" * 2, 45), ("B" * 4, 90), ("B" * 5, 120)],
)
def test_checkout_item_B(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize("skus,expected_amount", [("C", 20), ("C" * 3, 60)])
def test_checkout_item_C(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize("skus,expected_amount", [("D", 15), ("D" * 3, 45)])
def test_checkout_item_D(skus, expected_amount):
    assert checkout(skus) == expected_amount



@pytest.mark.parametrize("skus,expected_amount", [("E", 40), ("E" * 3, 120)])
def test_checkout_item_E(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize("items", ["AAx", "e", "XYZ", "123"])
def test_checkout_invalid_items(items):
    assert checkout(items) == -1


@pytest.mark.parametrize("items", ["a", "b", "c", "d", "Aa", "Ab", "Ac", "Ad", "ABCDe"])
def test_checkout_lowercase_items(items):
    assert checkout(items) == -1


@pytest.mark.parametrize("items", list("- %^&*()"))
def test_checkout_invalid_chars(items):
    assert checkout(items) == -1


def test_checkout_no_item():
    assert checkout("") == 0

@pytest.mark.parametrize("items,expected_amount", 
    [
        ("EE", 80),
    ]
)
def test_checkout_free_items(items):
    assert checkout(items) == 0





