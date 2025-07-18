import pytest
from solutions.solution_48 import my_sqrt

@pytest.mark.parametrize("x, expected", [
    (4, 2),
    (8, 2),
    (0, 0),
    (1, 1),
    (2, 1),
    (9, 3),
    (2147395599, 46339)
])
def test_my_sqrt(x, expected):
    assert my_sqrt(x) == expected