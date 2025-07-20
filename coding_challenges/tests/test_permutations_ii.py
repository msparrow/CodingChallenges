
import pytest
from solutions.solution_34 import permute_unique

@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2], sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])),
    ([1, 2, 3], sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])),
    ([1, 1, 1], [[1, 1, 1]]),
    ([1, 1, 2, 2], sorted([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]])),
    ([1, 2, 1], sorted([[1, 1, 2], [1, 2, 1], [2, 1, 1]])),
    ([2, 2, 1, 1], sorted([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]])),
    ([3, 3, 0, 3], sorted([[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]])),
    ([1], [[1]]),
    ([], [[]])
])
def test_permute_unique(nums, expected):
    result = permute_unique(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
