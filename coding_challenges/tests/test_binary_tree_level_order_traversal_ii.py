import pytest
from solutions.solution_88 import level_order_bottom, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[15, 7], [9, 20], [3]]),
    (TreeNode(1), [[1]]),
    (None, [])
])
def test_level_order_bottom(root, expected):
    assert level_order_bottom(root) == expected