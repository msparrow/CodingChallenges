
import pytest
from solutions.solution_92 import min_depth, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 2),
    (TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), 5),
    (None, 0),
    (TreeNode(1), 1),
    (TreeNode(1, TreeNode(2)), 2),
    (TreeNode(1, None, TreeNode(2)), 2),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 2),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 2),
    (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5))), 2),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), 2),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5))), 3),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)))), 3),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5, TreeNode(7)))), 3),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), 3),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), None)), 3),
    (TreeNode(4, TreeNode(2, TreeNode(1), None), TreeNode(6, TreeNode(5), TreeNode(7))), 3),
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), 3),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None), 2),
    (TreeNode(4, None, TreeNode(6, TreeNode(5), TreeNode(7))), 3),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), 5)
])
def test_min_depth(root, expected):
    assert min_depth(root) == expected
