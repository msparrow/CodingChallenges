
import pytest
from solutions.solution_76 import generate_trees, TreeNode

# This is a difficult problem to test because the output is a list of trees.
# For now, we will just check the number of trees generated.
@pytest.mark.parametrize("n, expected_count", [
    (3, 5),
    (1, 1),
    (0, 1),  # Expecting a list with a single None
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
    (19, 1767263190)
])
def test_generate_trees(n, expected_count):
    assert len(generate_trees(n)) == expected_count
