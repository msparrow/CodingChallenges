
import pytest
from solutions.solution_94 import path_sum, TreeNode

@pytest.mark.parametrize("root, target_sum, expected", [
    (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22, sorted([[5, 4, 11, 2], [5, 8, 4, 5]])),
    (TreeNode(1, TreeNode(2), TreeNode(3)), 5, []),
    (None, 0, [])
])
def test_path_sum(root, target_sum, expected):
    result = path_sum(root, target_sum)
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
