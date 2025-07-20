
import pytest
from solutions.solution_75 import inorder_traversal, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 3, 2]),
    (None, []),
    (TreeNode(1), [1]),
    (TreeNode(1, TreeNode(2)), [2, 1]),
    (TreeNode(1, None, TreeNode(2)), [1, 2]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [2, 1, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [4, 2, 1, 3]),
    (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5))), [2, 1, 5, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), [4, 2, 1, 5, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5))), [6, 4, 2, 1, 5, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)))), [4, 2, 1, 5, 7, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5, TreeNode(7)))), [6, 4, 2, 1, 5, 7, 3]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [1, 2, 3, 4, 5, 6, 7]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), None)), [1, 2, 3, 4, 5, 6]),
    (TreeNode(4, TreeNode(2, TreeNode(1), None), TreeNode(6, TreeNode(5), TreeNode(7))), [1, 2, 4, 5, 6, 7]),
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [2, 3, 4, 5, 6, 7]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None), [1, 2, 3, 4]),
    (TreeNode(4, None, TreeNode(6, TreeNode(5), TreeNode(7))), [4, 5, 6, 7]),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), [5, 4, 3, 2, 1])
])
def test_inorder_traversal(root, expected):
    assert inorder_traversal(root) == expected
