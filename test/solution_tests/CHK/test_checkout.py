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
        ("AA", 100),
        ("AAA", 130),
        ("AAAA", 180),
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


@pytest.mark.parametrize(
    "skus,expected_amount", [("H", 10), ("HH", 20), ("H" * 5, 45), ("H" * 10, 80)]
)
def test_checkout_item_H(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize("skus,expected_amount", [("K", 80), ("KK", 150), ("KKK", 230)])
def test_checkout_item_K(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("N", 40), ("NN", 80), ("NNN", 120), ("NNNM", 120)]
)
def test_checkout_item_N(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("P", 50), ("PP", 100), ("P" * 5, 200), ("P" * 6, 250)]
)
def test_checkout_item_P(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("Q", 30), ("QQ", 60), ("Q" * 3, 80), ("Q" * 4, 110)]
)
def test_checkout_item_Q(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("R", 50), ("RR", 100), ("RRR", 150), ("RRRQ", 150)]
)
def test_checkout_item_R(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("U", 40), ("UU", 80), ("UUU", 120), ("UUUU", 120)]
)
def test_checkout_item_U(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "skus,expected_amount", [("V", 50), ("VV", 90), ("VVV", 130), ("VVVV", 180)]
)
def test_checkout_item_V(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize("items", ["AAx", "e", "123"])
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


@pytest.mark.parametrize(
    "skus,expected_amount",
    [
        ("ABCXYZ", 145),
        ("ABCXYZZ", 162),
        ("ABCXXYZ", 162),
        ("ABCXYYZ", 162),
        ("ABCXXSY", 162),
        ("ABCXTSY", 162),
        ("XYZSTX", 90),
        ("XYZSTXZ", 107),
    ],
)
def test_checkout_group_discount(skus, expected_amount):
    assert checkout(skus) == expected_amount


@pytest.mark.parametrize(
    "items,expected_amount",
    [
        ("EE", 80),
        ("EEB", 80),
        ("BEE", 80),
        ("BBBEEEE", 190),
        ("BBBEE", 125),
    ],
)
def test_checkout_free_items(items, expected_amount):
    assert checkout(items) == expected_amount


@pytest.mark.parametrize(
    "items,expected_amount",
    [
        ("FF", 20),
        ("FFF", 20),
        ("FFFF", 30),
        ("FFFFFF", 40),
    ],
)
def test_checkout_buy_two_get_one_free(items, expected_amount):
    assert checkout(items) == expected_amount
