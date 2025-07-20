import pytest
from solutions.solution_82 import is_symmetric, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))), True),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))), False),
    (None, True),
    (TreeNode(1), True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), False),
    (TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3))), True),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, TreeNode(3))), False),
    (TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, TreeNode(3))), False),
    (TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(3, TreeNode(4))), True),
    (TreeNode(2, TreeNode(3, None, TreeNode(4)), TreeNode(3, None, TreeNode(4))), True),
    (TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(3, None, TreeNode(4))), False),
    (TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2))), True),
    (TreeNode(1, TreeNode(2, None, TreeNode(2)), TreeNode(2, None, TreeNode(2))), True),
    (TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, None, TreeNode(2))), False),
    (TreeNode(1, TreeNode(0)), False),
    (TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, None, TreeNode(3))), False),
    (TreeNode(5, TreeNode(4, None, TreeNode(3)), TreeNode(4, None, TreeNode(3))), False),
    (TreeNode(5, TreeNode(4, TreeNode(3)), TreeNode(4, TreeNode(3))), True),
    (TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3))), False),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3))), False)
])
def test_is_symmetric(root, expected):
    assert is_symmetric(root) == expected