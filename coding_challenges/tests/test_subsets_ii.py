
import pytest
from solutions.solution_71 import subsets_with_dup

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2], sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])),
    ([0], sorted([[], [0]])),
    ([4, 4, 4, 1, 4], sorted([[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]])),
    ([], [[]]),
    ([1, 1], sorted([[], [1], [1, 1]])),
    ([1, 1, 1], sorted([[], [1], [1, 1], [1, 1, 1]])),
    ([1, 2, 3], sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])),
    ([-1, 1, 2], sorted([[], [-1], [1], [2], [-1, 1], [-1, 2], [1, 2], [-1, 1, 2]])),
    ([-1, -1, 2], sorted([[], [-1], [-1, -1], [2], [-1, 2], [-1, -1, 2]])),
    ([2, 2, 2], sorted([[], [2], [2, 2], [2, 2, 2]])),
    ([1, 1, 2, 2], sorted([[], [1], [1, 1], [2], [2, 2], [1, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]])),
    ([5, 5, 5, 5, 5], sorted([[], [5], [5, 5], [5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5, 5]])),
    ([1, 5, 1], sorted([[], [1], [1, 1], [5], [1, 5], [1, 1, 5]])),
    ([3, 3, 1, 3], sorted([[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [3, 3, 3], [1, 3, 3, 3]])),
    ([1, 2, 2, 3], sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 2], [2, 3], [1, 2, 2], [1, 2, 3], [2, 2, 3], [1, 2, 2, 3]])),
    ([0, 0, 0], sorted([[], [0], [0, 0], [0, 0, 0]])),
    ([1, 1, 0], sorted([[], [0], [1], [0, 1], [1, 1], [0, 1, 1]])),
    ([-1, 1, -1], sorted([[], [-1], [1], [-1, -1], [-1, 1], [-1, -1, 1]])),
    ([10, 1, 10], sorted([[], [1], [10], [1, 10], [10, 10], [1, 10, 10]])),
    ([1, 2, 1, 2], sorted([[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]))
])
def test_subsets_with_dup(nums, expected):
    result = subsets_with_dup(nums)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
