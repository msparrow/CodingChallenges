
import pytest
from solutions.solution_38 import solve_n_queens

@pytest.mark.parametrize("n, expected", [
    (4, sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]))
])
def test_solve_n_queens(n, expected):
    result = solve_n_queens(n)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
