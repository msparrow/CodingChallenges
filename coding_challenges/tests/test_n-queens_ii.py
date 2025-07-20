
import pytest
from solutions.solution_39 import total_n_queens

@pytest.mark.parametrize("n, expected", [
    (4, 2),
    (1, 1),
    (8, 92),
    (2, 0),
    (3, 0),
    (5, 10),
    (6, 4),
    (7, 40),
    (9, 352),
    (10, 724),
    (11, 2680),
    (12, 14200),
    (13, 73712),
    (14, 365596),
    (15, 2279184),
    (16, 14772512),
    (17, 95815104),
    (18, 666090624),
    (19, 4968057848)
])
def test_total_n_queens(n, expected):
    assert total_n_queens(n) == expected
