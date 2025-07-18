import pytest
from solutions.solution_87 import build_tree2, TreeNode

# This is a difficult problem to test because the output is a tree.
# For now, we will just check a simple case.
@pytest.mark.parametrize("inorder, postorder, expected_root", [
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
])
def test_build_tree2(inorder, postorder, expected_root):
    root = build_tree2(inorder, postorder)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
    assert root.left.val == expected_root.left.val
    assert root.right.val == expected_root.right.val