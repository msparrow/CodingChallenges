
import pytest
from solutions.solution_91 import is_balanced, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), True),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)), False),
    (None, True),
    (TreeNode(1, TreeNode(2), None), True),
    (TreeNode(1, None, TreeNode(2)), True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), True),
    (TreeNode(1, TreeNode(2, TreeNode(3)), None), False),
    (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), False),
    (TreeNode(1, TreeNode(2, None, TreeNode(3)), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), None), False),
    (TreeNode(1, TreeNode(2, None, TreeNode(3, None, TreeNode(4))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))), None), False),
    (TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4, None, TreeNode(5)))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4, None, TreeNode(5)))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), None), False),
    (TreeNode(1, TreeNode(2, None, TreeNode(3, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), None), False),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, None, TreeNode(5, None, TreeNode(6, None, TreeNode(7)))))), None), False)
])
def test_is_balanced(root, expected):
    assert is_balanced(root) == expected
