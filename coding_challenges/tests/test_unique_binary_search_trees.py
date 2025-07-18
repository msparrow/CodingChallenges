
import pytest
from solutions.solution_77 import num_trees

@pytest.mark.parametrize("n, expected", [
    (3, 5),
    (1, 1),
    (4, 14)
])
def test_num_trees(n, expected):
    assert num_trees(n) == expected
