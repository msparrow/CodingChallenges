
import pytest
from solutions.solution_92 import min_depth, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 2),
    (TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), 5),
    (None, 0)
])
def test_min_depth(root, expected):
    assert min_depth(root) == expected
