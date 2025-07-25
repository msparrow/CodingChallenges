
import pytest
from solutions.solution_93 import has_path_sum, TreeNode

@pytest.mark.parametrize("root, target_sum, expected", [
    (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22, True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 5, False),
    (None, 0, False),
    (TreeNode(1), 1, True),
    (TreeNode(1), 0, False),
    (TreeNode(1, TreeNode(2)), 3, True),
    (TreeNode(1, TreeNode(2)), 1, False),
    (TreeNode(1, None, TreeNode(2)), 3, True),
    (TreeNode(1, None, TreeNode(2)), 1, False),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 3, True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 4, True),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 5, False),
    (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 26, True),
    (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 18, True),
    (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 27, False),
    (TreeNode(1, TreeNode(2)), 0, False),
    (TreeNode(1, TreeNode(2)), 1, False),
    (TreeNode(1, TreeNode(2)), 2, False),
    (TreeNode(1, TreeNode(2)), 3, True)
])
def test_has_path_sum(root, target_sum, expected):
    assert has_path_sum(root, target_sum) == expected
