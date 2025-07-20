
import pytest
from solutions.solution_77 import num_trees

@pytest.mark.parametrize("n, expected", [
    (3, 5),
    (1, 1),
    (2, 2),
    (4, 14),
    (5, 42),
    (6, 132),
    (7, 429),
    (8, 1430),
    (9, 4862),
    (10, 16796),
    (11, 58786),
    (12, 208012),
    (13, 742900),
    (14, 2674440),
    (15, 9694845),
    (16, 35357670),
    (17, 129644790),
    (18, 477638700),
    (19, 1767263190),
    (0, 1)
])
def test_num_trees(n, expected):
    assert num_trees(n) == expected
