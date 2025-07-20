import pytest
from solutions.solution_48 import my_sqrt

@pytest.mark.parametrize("x, expected", [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (2, 1),
    (9, 3),
    (16, 4),
    (25, 5),
    (36, 6),
    (49, 7),
    (64, 8),
    (81, 9),
    (100, 10),
    (121, 11),
    (144, 12),
    (169, 13),
    (196, 14),
    (225, 15),
    (256, 16),
    (2147395599, 46339)
])
def test_my_sqrt(x, expected):
    assert my_sqrt(x) == expected