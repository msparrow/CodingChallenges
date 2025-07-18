import pytest
from solutions.solution_85 import max_depth, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 3),
    (TreeNode(1, None, TreeNode(2)), 2),
    (None, 0)
])
def test_max_depth(root, expected):
    assert max_depth(root) == expected