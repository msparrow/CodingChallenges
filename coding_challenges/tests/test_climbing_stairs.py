import pytest
from solutions.solution_49 import climb_stairs

@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3),
    (1, 1),
    (4, 5),
    (5, 8),
    (6, 13),
    (7, 21),
    (8, 34),
    (9, 55),
    (10, 89),
    (11, 144),
    (12, 233),
    (13, 377),
    (14, 610),
    (15, 987),
    (16, 1597),
    (17, 2584),
    (18, 4181),
    (19, 6765),
    (20, 10946)
])
def test_climb_stairs(n, expected):
    assert climb_stairs(n) == expected