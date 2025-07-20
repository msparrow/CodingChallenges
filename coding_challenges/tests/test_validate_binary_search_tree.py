
import pytest
from solutions.solution_79 import is_valid_bst, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(2, TreeNode(1), TreeNode(3)), True),
    (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    (TreeNode(2, TreeNode(2), TreeNode(2)), False),
    (TreeNode(1, None, TreeNode(1)), False),
    (None, True),
    (TreeNode(0), True),
    (TreeNode(1, TreeNode(0)), True),
    (TreeNode(1, None, TreeNode(2)), True),
    (TreeNode(1, TreeNode(2)), False),
    (TreeNode(1, None, TreeNode(0)), False),
    (TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20))), True),
    (TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(12)), TreeNode(15, TreeNode(7), TreeNode(20))), False),
    (TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))), True),
    (TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(4)), TreeNode(5, TreeNode(2), TreeNode(6))), False),
    (TreeNode(2147483647), True),
    (TreeNode(-2147483648), True),
    (TreeNode(0, TreeNode(-1)), True),
    (TreeNode(0, None, TreeNode(1)), True),
    (TreeNode(1, TreeNode(1)), False),
    (TreeNode(1, None, TreeNode(1)), False)
])
def test_is_valid_bst(root, expected):
    assert is_valid_bst(root) == expected
