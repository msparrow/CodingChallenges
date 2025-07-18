
import pytest
from solutions.solution_39 import total_n_queens

@pytest.mark.parametrize("n, expected", [
    (4, 2),
    (1, 1),
    (8, 92)
])
def test_total_n_queens(n, expected):
    assert total_n_queens(n) == expected
