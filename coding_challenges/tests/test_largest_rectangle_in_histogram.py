
import pytest
from solutions.solution_65 import largest_rectangle_area

@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([2, 1, 2], 3),
    ([2, 1, 5, 6, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 26),
    ([6, 2, 5, 4, 5, 1, 6], 12),
    ([1, 2, 3, 4, 5], 9),
    ([5, 4, 3, 2, 1], 9),
    ([1, 1, 1, 1, 1], 5),
    ([0, 0, 0, 0, 0], 0),
    ([1, 2, 1, 2, 1, 2], 6),
    ([2, 1, 2, 1, 2, 1], 6),
    ([1, 2, 3, 2, 1], 5),
    ([1, 3, 2, 1, 2], 5),
    ([3, 1, 3, 2, 2], 6),
    ([2, 1, 5, 6, 2, 3], 10),
    ([4, 2, 0, 3, 2, 5], 6),
    ([1, 1, 1, 5, 1, 1, 1], 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 30),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 30)
])
def test_largest_rectangle_area(heights, expected):
    assert largest_rectangle_area(heights) == expected
