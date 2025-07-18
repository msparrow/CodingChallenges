
import pytest
from solutions.solution_76 import generate_trees, TreeNode

# This is a difficult problem to test because the output is a list of trees.
# For now, we will just check the number of trees generated.
@pytest.mark.parametrize("n, expected_count", [
    (3, 5),
    (1, 1)
])
def test_generate_trees(n, expected_count):
    assert len(generate_trees(n)) == expected_count
