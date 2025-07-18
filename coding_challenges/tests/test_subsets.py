import pytest
from solutions.solution_57 import subsets

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])),
    ([0], sorted([[], [0]])),
    ([1, 2], sorted([[], [1], [2], [1, 2]]))
])
def test_subsets(nums, expected):
    result = subsets(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])