
import pytest
from solutions.solution_71 import subsets_with_dup

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2], sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])),
    ([0], sorted([[], [0]])),
    ([4, 4, 4, 1, 4], sorted([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])) 
])
def test_subsets_with_dup(nums, expected):
    result = subsets_with_dup(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
