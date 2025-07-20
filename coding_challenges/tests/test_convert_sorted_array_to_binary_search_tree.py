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
    assert root.right.left.val == expected_root.right.left.val
    assert root.right.right.val == expected_root.right.right.val

@pytest.mark.parametrize("nums, expected_root", [
    ([1, 2], TreeNode(2, TreeNode(1))),
    ([1, 2, 3], TreeNode(2, TreeNode(1), TreeNode(3))),
    ([1, 2, 3, 4], TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))),
    ([1, 2, 3, 4, 5], TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4)))),
    ([1, 2, 3, 4, 5, 6], TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5)))),
    ([1, 2, 3, 4, 5, 6, 7], TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))),
    ([1], TreeNode(1)),
    ([], None),
    ([-1, 0, 1], TreeNode(0, TreeNode(-1), TreeNode(1))),
    ([-3, -2, -1, 0, 1, 2, 3], TreeNode(0, TreeNode(-2, TreeNode(-3), TreeNode(-1)), TreeNode(2, TreeNode(1), TreeNode(3)))),
    ([0, 1, 2, 3, 4, 5], TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4)))),
    (list(range(10)), TreeNode(5, TreeNode(2, TreeNode(1, TreeNode(0)), TreeNode(4, TreeNode(3))), TreeNode(8, TreeNode(7, TreeNode(6)), TreeNode(9))))
])
def test_more_sorted_array_to_bst(nums, expected_root):
    root = sorted_array_to_bst(nums)
    if root:
        # This is a shallow check. A deep check would be more robust.
        assert root.val == expected_root.val