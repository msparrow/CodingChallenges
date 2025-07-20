
import pytest
from solutions.solution_29 import first_missing_positive

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([], 1),
    ([1], 2),
    ([2], 1),
    ([1, 1, 1], 2),
    ([1, 2, 3, 4, 5], 6),
    ([1, 2, 3, 5], 4),
    ([1, 1, 2, 2], 3),
    ([-1, -2, -3], 1),
    ([10, 20, 30], 1),
    ([1, 1000], 2),
    ([2, 3, 4], 1),
    ([1, 2, 3], 4),
    ([0, 1, 2], 3),
    ([0, 2, 1], 3),
    ([3, 4, -1, 1, 5, 6], 2),
    ([1, 2, 6, 3, 5, 4], 7)
])
def test_first_missing_positive(nums, expected):
    assert first_missing_positive(nums) == expected
