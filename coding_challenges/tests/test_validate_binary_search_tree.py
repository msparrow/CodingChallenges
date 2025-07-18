
import pytest
from solutions.solution_79 import is_valid_bst, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(2, TreeNode(1), TreeNode(3)), True),
    (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    (TreeNode(2, TreeNode(2), TreeNode(2)), False),
    (TreeNode(1, None, TreeNode(1)), False)
])
def test_is_valid_bst(root, expected):
    assert is_valid_bst(root) == expected
