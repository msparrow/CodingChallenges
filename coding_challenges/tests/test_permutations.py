
import pytest
from solutions.solution_33 import permute

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])),
    ([0, 1], sorted([[0, 1], [1, 0]])),
    ([1], [[1]])
])
def test_permute(nums, expected):
    result = permute(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
