import pytest
from solutions.solution_83 import level_order, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[3], [9, 20], [15, 7]]),
    (TreeNode(1), [[1]]),
    (None, [])
])
def test_level_order(root, expected):
    assert level_order(root) == expected