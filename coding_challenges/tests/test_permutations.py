
import pytest
from solutions.solution_33 import permute

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])),
    ([0, 1], sorted([[0, 1], [1, 0]])),
    ([1], [[1]]),
    ([1, 2], sorted([[1, 2], [2, 1]])),
    ([1, 2, 3, 4], sorted([[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]])),
    ([], [[]])
])
def test_permute(nums, expected):
    result = permute(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
