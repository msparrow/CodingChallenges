
import pytest
from solutions.solution_29 import first_missing_positive

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 0], 3),
    ([3, 4, -1, 1], 2),
    ([7, 8, 9, 11, 12], 1),
    ([], 1),
    ([1], 2),
    ([2], 1),
    ([1, 1, 1], 2)
])
def test_first_missing_positive(nums, expected):
    assert first_missing_positive(nums) == expected
