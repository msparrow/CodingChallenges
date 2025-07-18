import pytest
from solutions.solution_81 import is_same_tree, TreeNode

@pytest.mark.parametrize("p, q, expected", [
    (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)), True),
    (TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)), False),
    (TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2)), False)
])
def test_is_same_tree(p, q, expected):
    assert is_same_tree(p, q) == expected