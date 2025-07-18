
import pytest
from solutions.solution_91 import is_balanced, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), True),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)), False),
    (None, True)
])
def test_is_balanced(root, expected):
    assert is_balanced(root) == expected
