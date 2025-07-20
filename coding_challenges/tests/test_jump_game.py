import pytest
from solutions.solution_42 import can_jump

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([0], True),
    ([1], True),
    ([2, 0, 0], True),
    ([2, 5, 0, 0], True),
    ([1, 1, 1, 1], True),
    ([1, 1, 1, 0], True),
    ([1, 1, 0, 1], False),
    ([1, 0, 1, 0], False),
    ([5, 4, 3, 2, 1, 0, 0], False),
    ([1, 2, 3, 4, 5], True),
    ([0, 1, 2, 3, 4], False),
    ([4, 3, 2, 1, 0], True),
    ([1, 1, 1, 1, 1, 1, 1, 0], True),
    ([1, 0, 1], False),
    ([2, 0, 1], True),
    ([2, 1, 0, 2], False),
    ([3, 0, 8, 2, 5, 0, 3, 4, 1, 1, 0, 2], True),
    ([4, 2, 0, 0, 1, 1, 4, 4, 4, 0, 4, 0], True)
])
def test_can_jump(nums, expected):
    assert can_jump(nums) == expected