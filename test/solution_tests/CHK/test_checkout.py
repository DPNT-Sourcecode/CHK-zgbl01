import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize("skus,expected_amount", [("A"*3, 130), ("A"*6, 260), ("A"*8, 360)])
def test_checkout_special_offer_A(skus, expected_amount):
    assert checkout(skus) == expected_amount 


@pytest.mark.parametrize("skus,expected_amount", [("B"*2, 45), ("B"*4, 90), ("B"*5, 120)])
def test_checkout_special_offer_A(skus, expected_amount):
    assert checkout(skus) == expected_amount 


