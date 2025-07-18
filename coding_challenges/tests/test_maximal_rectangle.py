
import pytest
from solutions.solution_66 import maximal_rectangle

@pytest.mark.parametrize("matrix, expected", [
    ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["0","0"]], 0),
    ([["1","1"]], 2)
])
def test_maximal_rectangle(matrix, expected):
    assert maximal_rectangle(matrix) == expected
