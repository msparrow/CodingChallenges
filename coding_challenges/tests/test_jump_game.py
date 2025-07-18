import pytest
from solutions.solution_42 import can_jump

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0], True),
    ([1], True),
    ([2, 0, 0], True),
    ([2, 5, 0, 0], True)
])
def test_can_jump(nums, expected):
    assert can_jump(nums) == expected