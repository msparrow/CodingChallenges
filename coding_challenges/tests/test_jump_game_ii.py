
import pytest
from solutions.solution_32 import jump

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], 2),
    ([2, 3, 0, 1, 4], 2),
    ([1, 1, 1, 1, 1], 4),
    ([1, 2, 3, 4, 5], 3),
    ([5, 4, 3, 2, 1], 1),
    ([1, 1, 1, 1, 0], 4)
])
def test_jump(nums, expected):
    assert jump(nums) == expected
