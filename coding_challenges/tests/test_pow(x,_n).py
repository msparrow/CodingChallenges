
import pytest
from solutions.solution_37 import my_pow

@pytest.mark.parametrize("x, n, expected", [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000),
    (0.00001, 2147483647, 0.0)
])
def test_my_pow(x, n, expected):
    assert my_pow(x, n) == pytest.approx(expected)
