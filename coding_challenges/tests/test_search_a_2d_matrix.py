
import pytest
from solutions.solution_53 import search_matrix

@pytest.mark.parametrize("matrix, target, expected", [
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
    ([], 0, False),
    ([[]], 0, False),
    ([[1]], 1, True),
    ([[1]], 0, False),
    ([[1, 2]], 1, True),
    ([[1, 2]], 2, True),
    ([[1, 2]], 0, False),
    ([[1, 2]], 3, False),
    ([[1], [2]], 1, True),
    ([[1], [2]], 2, True),
    ([[1], [2]], 0, False),
    ([[1], [2]], 3, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11, True),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 12, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 0, False),
    ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 60, False),
    ([[-10, -8, -6, -4], [-2, 0, 2, 4], [6, 8, 10, 12]], 0, True)
])
def test_search_matrix(matrix, target, expected):
    assert search_matrix(matrix, target) == expected
