import pytest
from lib.solutions.SUM import sum_solution


class TestSum:
    @pytest.mark.parametrize(
        "x,y,expected_value", [(0, 0, 0), (1, 2, 3), (50, 0, 50), (100, 100, 200)]
    )
    def test_sum(self, x, y, expected_value):
        assert sum_solution.compute(x, y) == expected_value

    def test_sum_answer_type(self):
        assert isinstance(sum_solution.compute(1, 2), int) 



