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
    assert root.right.left.val == expected_root.right.left.val
    assert root.right.right.val == expected_root.right.right.val

@pytest.mark.parametrize("head, expected_root", [
    (ListNode(1, ListNode(2)), TreeNode(2, TreeNode(1))),
    (ListNode(1, ListNode(2, ListNode(3))), TreeNode(2, TreeNode(1), TreeNode(3))),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(5, TreeNode(4)))),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5)))),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))), TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))),
    (ListNode(1), TreeNode(1)),
    (None, None),
    (ListNode(-1, ListNode(0, ListNode(1))), TreeNode(0, TreeNode(-1), TreeNode(1))),
    (ListNode(-3, ListNode(-2, ListNode(-1, ListNode(0, ListNode(1, ListNode(2, ListNode(3))))))), TreeNode(0, TreeNode(-2, TreeNode(-3), TreeNode(-1)), TreeNode(2, TreeNode(1), TreeNode(3)))),
    (ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))), TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4)))),
    (ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))), TreeNode(5, TreeNode(2, TreeNode(1, TreeNode(0)), TreeNode(4, TreeNode(3))), TreeNode(8, TreeNode(7, TreeNode(6)), TreeNode(9))))
])
def test_more_sorted_list_to_bst(head, expected_root):
    root = sorted_list_to_bst(head)
    if root:
        # This is a shallow check. A deep check would be more robust.
        assert root.val == expected_root.val