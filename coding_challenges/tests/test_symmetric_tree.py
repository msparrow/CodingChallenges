import pytest
from solutions.solution_82 import is_symmetric, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))), True),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))), False),
    (None, True)
])
def test_is_symmetric(root, expected):
    assert is_symmetric(root) == expected