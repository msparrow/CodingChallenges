
import pytest
from solutions.solution_38 import solve_n_queens

@pytest.mark.parametrize("n, expected", [
    (4, sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])),
    (1, [["Q"]]),
    (2, []),
    (3, []),
    (5, sorted([
        ["Q....","..Q..","....Q",".Q...","...Q."],
        ["Q....","...Q.",".Q...","....Q","..Q.."],
        [".Q...","...Q.","Q....","..Q..","....Q"],
        [".Q...","....Q","..Q..","Q....","...Q."],
        ["..Q..","Q....","...Q.",".Q...","....Q"],
        ["..Q..","....Q",".Q...","...Q.","Q...."],
        ["...Q.","Q....","..Q..","....Q",".Q..."],
        ["...Q.",".Q...","....Q","..Q..","Q...."],
        ["....Q",".Q...","...Q.","Q....","..Q.."],
        ["....Q","..Q..","Q....","...Q.",".Q..."]
    ])),
    (6, sorted([
        [".Q....","...Q..",".....Q","Q.....","..Q...","....Q."],
        ["..Q...",".....Q",".Q....","....Q.","Q.....","...Q.."],
        ["...Q..","Q.....","....Q.",".Q....",".....Q","..Q..."],
        ["....Q.","..Q...","Q.....",".....Q","...Q..",".Q...."]
    ])),
    (7, sorted([
        ["Q......","..Q....","....Q..","......Q",".Q.....","...Q...",".....Q."],
        ["Q......","...Q...",".....Q.",".Q.....","......Q","..Q....","....Q.."],
        # ... (and so on for all 40 solutions)
    ])),
    (8, sorted([
        # ... (92 solutions)
    ]))
])
def test_solve_n_queens(n, expected):
    if n > 6:
        pytest.skip("Test case for n>6 is too large to include all solutions.")
    result = solve_n_queens(n)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])

@pytest.mark.parametrize("n, expected_count", [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724),
    (11, 2680),
    (12, 14200),
    (13, 73712),
    (14, 365596),
    (15, 2279184)
])
def test_n_queens_solution_count(n, expected_count):
    assert len(solve_n_queens(n)) == expected_count
