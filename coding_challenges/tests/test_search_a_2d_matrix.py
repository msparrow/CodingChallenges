
import pytest
from solutions.solution_53 import search_matrix

@pytest.mark.parametrize("matrix, target, expected", [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([], 0, False),
    ([[]], 0, False)
])
def test_search_matrix(matrix, target, expected):
    assert search_matrix(matrix, target) == expected
