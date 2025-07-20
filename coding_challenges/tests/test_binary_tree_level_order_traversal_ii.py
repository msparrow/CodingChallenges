import pytest
from solutions.solution_88 import level_order_bottom, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[15, 7], [9, 20], [3]]),
    (TreeNode(1), [[1]]),
    (None, []),
    (TreeNode(1, TreeNode(2)), [[2], [1]]),
    (TreeNode(1, None, TreeNode(2)), [[2], [1]]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [[2, 3], [1]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [[4, 3], [2], [1]]),
    (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5))), [[5], [2, 3], [1]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), [[4, 5], [2, 3], [1]]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5))), [[6, 5], [4, 3], [2], [1]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)))), [[4, 7], [2, 5], [1, 3]]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5, TreeNode(7)))), [[6, 7], [4, 5], [2, 3], [1]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [[1, 3, 5, 7], [2, 6], [4]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), None)), [[1, 3, 5], [2, 6], [4]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), None), TreeNode(6, TreeNode(5), TreeNode(7))), [[1, 5, 7], [2, 6], [4]]),
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [[3, 5, 7], [2, 6], [4]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None), [[1, 3], [2], [4]]),
    (TreeNode(4, None, TreeNode(6, TreeNode(5), TreeNode(7))), [[5, 7], [6], [4]]),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), [[5], [4], [3], [2], [1]])
])
def test_level_order_bottom(root, expected):
    assert level_order_bottom(root) == expected