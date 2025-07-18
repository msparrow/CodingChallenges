
import pytest
from solutions.solution_24 import search_insert

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 0, 0)
])
def test_search_insert(nums, target, expected):
    assert search_insert(nums, target) == expected
