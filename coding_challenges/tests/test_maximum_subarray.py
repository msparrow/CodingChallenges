
import pytest
from solutions.solution_40 import max_sub_array

@pytest.mark.parametrize("nums, expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1], -1),
    ([-2, -1], -1)
])
def test_max_sub_array(nums, expected):
    assert max_sub_array(nums) == expected
