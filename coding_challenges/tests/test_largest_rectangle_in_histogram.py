
import pytest
from solutions.solution_65 import largest_rectangle_area

@pytest.mark.parametrize("heights, expected", [
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([2, 1, 2], 3),
    ([2, 1, 5, 6, 2, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 26)
])
def test_largest_rectangle_area(heights, expected):
    assert largest_rectangle_area(heights) == expected
