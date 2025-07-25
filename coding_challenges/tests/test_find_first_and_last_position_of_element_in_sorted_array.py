import pytest
from solutions.solution_62 import search_range

@pytest.mark.parametrize("nums, target, expected", [
    ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
    ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
    ([], 0, [-1, -1]),
    ([1], 1, [0, 0]),
    ([1, 1], 1, [0, 1]),
    ([1, 1, 1], 1, [0, 2]),
    ([1, 2, 3], 2, [1, 1]),
    ([1, 2, 3, 3, 3, 4, 5], 3, [2, 4]),
    ([1, 2, 3, 4, 5], 6, [-1, -1]),
    ([1, 2, 3, 4, 5], 0, [-1, -1]),
    ([1, 1, 1, 1, 1], 1, [0, 4]),
    ([1, 1, 2, 2, 2, 3, 3], 2, [2, 4]),
    ([1, 1, 2, 2, 2, 3, 3], 1, [0, 1]),
    ([1, 1, 2, 2, 2, 3, 3], 3, [5, 6]),
    ([1, 1, 2, 2, 2, 3, 3], 4, [-1, -1]),
    ([2, 2], 2, [0, 1]),
    ([2, 2], 3, [-1, -1]),
    ([2, 2], 1, [-1, -1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [4, 4])
])
def test_search_range(nums, target, expected):
    assert search_range(nums, target) == expected