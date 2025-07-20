import pytest
from solutions.solution_83 import level_order, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [[3], [9, 20], [15, 7]]),
    (TreeNode(1), [[1]]),
    (None, []),
    (TreeNode(1, TreeNode(2)), [[1], [2]]),
    (TreeNode(1, None, TreeNode(2)), [[1], [2]]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [[1], [2, 3]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [[1], [2], [4, 3]]),
    (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5))), [[1], [2, 3], [5]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), [[1], [2, 3], [4, 5]]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5))), [[1], [2], [4, 3], [6, 5]]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)))), [[1], [2, 3], [4, 5], [7]]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5, TreeNode(7)))), [[1], [2, 3], [4, 5], [6, 7]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [[4], [2, 6], [1, 3, 5, 7]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), None)), [[4], [2, 6], [1, 3, 5]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), None), TreeNode(6, TreeNode(5), TreeNode(7))), [[4], [2, 6], [1, 5, 7]]),
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [[4], [2, 6], [3, 5, 7]]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None), [[4], [2], [1, 3]]),
    (TreeNode(4, None, TreeNode(6, TreeNode(5), TreeNode(7))), [[4], [6], [5, 7]]),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), [[1], [2], [3], [4], [5]])
])
def test_level_order(root, expected):
    assert level_order(root) == expected