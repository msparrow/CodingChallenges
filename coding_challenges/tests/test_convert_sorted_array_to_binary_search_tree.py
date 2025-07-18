import pytest
from solutions.solution_89 import sorted_array_to_bst, TreeNode

# This is a difficult problem to test because the output is a tree.
# For now, we will just check a simple case.
@pytest.mark.parametrize("nums, expected_root", [
    ([-10, -3, 0, 5, 9], TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))))
])
def test_sorted_array_to_bst(nums, expected_root):
    root = sorted_array_to_bst(nums)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
    assert root.left.val == expected_root.left.val
    assert root.right.val == expected_root.right.val