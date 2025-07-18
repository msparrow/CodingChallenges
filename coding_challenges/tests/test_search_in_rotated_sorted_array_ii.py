import pytest
from solutions.solution_63 import search2

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 5, 6, 0, 0, 1, 2], 0, True),
    ([2, 5, 6, 0, 0, 1, 2], 3, False),
    ([1, 0, 1, 1, 1], 0, True),
    ([1, 1, 1, 0, 1], 0, True)
])
def test_search2(nums, target, expected):
    assert search2(nums, target) == expected