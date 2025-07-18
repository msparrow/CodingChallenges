
import pytest
from solutions.solution_30 import trap

@pytest.mark.parametrize("height, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
    ([4, 2, 0, 3, 2, 5], 9),
    ([], 0),
    ([1, 1, 1], 0),
    ([1, 0, 1], 1),
    ([1, 2, 1], 0),
    ([5, 4, 1, 2], 1),
    ([5, 2, 1, 2, 1, 5], 14)
])
def test_trap(height, expected):
    assert trap(height) == expected
