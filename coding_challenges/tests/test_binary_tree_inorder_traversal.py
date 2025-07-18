
import pytest
from solutions.solution_75 import inorder_traversal, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 3, 2]),
    (None, []),
    (TreeNode(1), [1])
])
def test_inorder_traversal(root, expected):
    assert inorder_traversal(root) == expected
