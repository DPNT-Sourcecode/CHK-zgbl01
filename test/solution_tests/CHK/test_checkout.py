import pytest

from lib.solutions.CHK.checkout_solution import checkout


"""
In production codebase, I would also mock PRICE and SPECIAL_OFFERS config, so that
the tests are not dependent on the config.  
"""

@pytest.mark.parametrize("skus,expected_amount", [("A", 50), ("A"*3, 130), ("A"*6, 260), ("A"*8, 360)])
def test_checkout_item_A(skus, expected_amount):
    assert checkout(skus) == expected_amount 


@pytest.mark.parametrize("skus,expected_amount", [("B"*1, 30), ("B"*2, 45), ("B"*4, 90), ("B"*5, 120)])
def test_checkout_item_B(skus, expected_amount):
    assert checkout(skus) == expected_amount 


@pytest.mark.parametrize("skus,expected_amount", [("C", 20), ("C"*3, 60)])
def test_checkout_item_C(skus, expected_amount):
    assert checkout(skus) == expected_amount 


@pytest.mark.parametrize("skus,expected_amount", [("D", 15), ("D"*3, 45)])
def test_checkout_item_D(skus, expected_amount):
    assert checkout(skus) == expected_amount 


def test_checkout_invalid_items():
    assert checkout("ABCDE") == -1 


