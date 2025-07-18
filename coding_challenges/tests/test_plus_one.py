import pytest
from solutions.solution_46 import plus_one

@pytest.mark.parametrize("digits, expected", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([9, 9], [1, 0, 0]),
    ([0], [1])
])
def test_plus_one(digits, expected):
    assert plus_one(digits) == expected