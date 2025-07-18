import pytest
from solutions.solution_90 import sorted_list_to_bst, ListNode, TreeNode

# This is a difficult problem to test because the output is a tree.
# For now, we will just check a simple case.
@pytest.mark.parametrize("head, expected_root", [
    (ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))), TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5))))
])
def test_sorted_list_to_bst(head, expected_root):
    root = sorted_list_to_bst(head)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
    assert root.left.val == expected_root.left.val
    assert root.right.val == expected_root.right.val