import pytest
from solutions.solution_61 import search

@pytest.mark.parametrize("nums, target, expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([1, 3], 3, 1),
    ([3, 1], 1, 1),
    ([5, 1, 3], 5, 0),
    ([5, 1, 3], 1, 1),
    ([5, 1, 3], 3, 2),
    ([5, 1, 3], 0, -1),
    ([1, 3, 5], 1, 0),
    ([1, 3, 5], 3, 1),
    ([1, 3, 5], 5, 2),
    ([1, 3, 5], 0, -1),
    ([4, 5, 6, 7, 8, 1, 2, 3], 8, 4),
    ([4, 5, 6, 7, 8, 1, 2, 3], 2, 6),
    ([4, 5, 6, 7, 8, 1, 2, 3], 9, -1),
    ([1], 1, 0),
    ([1], 0, -1)
])
def test_search(nums, target, expected):
    assert search(nums, target) == expected