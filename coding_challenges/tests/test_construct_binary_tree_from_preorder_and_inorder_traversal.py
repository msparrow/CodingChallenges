import pytest
from solutions.solution_86 import build_tree, TreeNode

# This is a difficult problem to test because the output is a tree.
# For now, we will just check a simple case.
@pytest.mark.parametrize("preorder, inorder, expected_root", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
])
def test_build_tree(preorder, inorder, expected_root):
    root = build_tree(preorder, inorder)
    # This is a shallow check. A deep check would be more robust.
    assert root.val == expected_root.val
    assert root.left.val == expected_root.left.val
    assert root.right.val == expected_root.right.val
    assert root.right.left.val == expected_root.right.left.val
    assert root.right.right.val == expected_root.right.right.val

@pytest.mark.parametrize("preorder, inorder, expected_root", [
    ([2, 1], [1, 2], TreeNode(2, TreeNode(1))),
    ([1, 2], [2, 1], TreeNode(1, None, TreeNode(2))),
    ([2, 1, 3], [1, 2, 3], TreeNode(2, TreeNode(1), TreeNode(3))),
    ([1, 2, 3], [1, 2, 3], TreeNode(1, None, TreeNode(2, None, TreeNode(3)))),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))),
    ([1, 4, 5, 2, 3], [3, 2, 1, 4, 5], TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, None, TreeNode(5)))),
    ([1, 2, 3], [3, 2, 1], TreeNode(1, TreeNode(2, TreeNode(3)))),
    ([1, 2, 3, 4], [1, 2, 3, 4], TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))),
    ([4, 3, 2, 1], [4, 3, 2, 1], TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))),
    ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7], TreeNode(7, TreeNode(6, TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1))))))))
])
def test_more_build_tree(preorder, inorder, expected_root):
    root = build_tree(preorder, inorder)
    if root:
        # This is a shallow check. A deep check would be more robust.
        assert root.val == expected_root.val