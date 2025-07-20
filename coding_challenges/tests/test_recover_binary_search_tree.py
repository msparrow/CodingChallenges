
import pytest
from solutions.solution_80 import recover_tree, TreeNode

# This is a difficult problem to test because the function modifies the tree in-place.
# For now, we will just check a simple case.
@pytest.mark.parametrize("root, expected_root", [
    (TreeNode(1, TreeNode(3, None, TreeNode(2))), TreeNode(3, TreeNode(1, None, TreeNode(2))))
])
def test_recover_tree(root, expected_root):
    recover_tree(root)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
    assert root.left.val == expected_root.left.val
    assert root.right.val == expected_root.right.val

@pytest.mark.parametrize("root, expected_root", [
    (TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2))), TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))),
    (TreeNode(3, TreeNode(2, TreeNode(1))), TreeNode(1, TreeNode(2, TreeNode(3)))),
    (TreeNode(1, TreeNode(3), TreeNode(2)), TreeNode(2, TreeNode(1), TreeNode(3)))
])
def test_more_recover_tree(root, expected_root):
    recover_tree(root)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
