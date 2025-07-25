
import pytest
from solutions.solution_24 import search_insert

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([1], 0, 0),
    ([], 5, 0),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, 5),
    ([1, 2, 3, 4, 5], 0, 0),
    ([1, 3, 5, 7, 9], 4, 2),
    ([1, 3, 5, 7, 9], 10, 5),
    ([1, 3, 5, 7, 9], 0, 0),
    ([2, 4, 6, 8], 1, 0),
    ([2, 4, 6, 8], 9, 4),
    ([2, 4, 6, 8], 5, 2),
    ([10, 20, 30], 15, 1),
    ([10, 20, 30], 35, 3),
    ([10, 20, 30], 5, 0),
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, 2)
])
def test_search_insert(nums, target, expected):
    assert search_insert(nums, target) == expected
