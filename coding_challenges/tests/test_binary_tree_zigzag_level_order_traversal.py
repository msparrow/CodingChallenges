import pytest
from solutions.solution_84 import zigzag_level_order, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[3], [20, 9], [15, 7]]),
    (TreeNode(1), [[1]]),
    (None, [])
])
def test_zigzag_level_order(root, expected):
    assert zigzag_level_order(root) == expected