
import pytest
from solutions.solution_13 import four_sum

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 0, -1, 0, -2, 2], 0, sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])),
    ([2, 2, 2, 2, 2], 8, sorted([[2, 2, 2, 2]])),
    ([1, 2, 3, 4], 10, sorted([[1, 2, 3, 4]])),
    ([-2, -1, 0, 1, 2], 0, sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])),
    ([-3, -1, 0, 2, 4, 5], 0, sorted([[-3, -1, 0, 4]])),
    ([-3, -1, 0, 2, 4, 5], 1, sorted([[-3, -1, 0, 5], [-3, -1, 2, 2]])),
    ([0, 0, 0, 0], 0, sorted([[0, 0, 0, 0]])),
    ([-1, 0, 1, 2, -1, -4], -1, sorted([[-4, 0, 1, 2], [-1, -1, 0, 1]])),
    ([1, -2, -5, -4, -3, 3, 3, 5], -11, sorted([[-5, -4, -3, 1]])),
    ([0, 0, 0, 1000000000, 1000000000, 1000000000, 1000000000], 1000000000, sorted([[0, 0, 0, 1000000000]]))
])
def test_four_sum(nums, target, expected):
    result = four_sum(nums, target)
    # Sort the inner lists and the outer list to make the test deterministic
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])