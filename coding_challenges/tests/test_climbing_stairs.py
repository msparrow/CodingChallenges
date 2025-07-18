import pytest
from solutions.solution_49 import climb_stairs

@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3),
    (1, 1),
    (4, 5),
    (5, 8)
])
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected