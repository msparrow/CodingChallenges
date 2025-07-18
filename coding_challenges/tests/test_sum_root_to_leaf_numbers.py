
import pytest
from solutions.solution_98 import sum_numbers, TreeNode

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 25),
    (TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)), 1026)
])
def test_sum_numbers(root, expected):
    assert sum_numbers(root) == expected
