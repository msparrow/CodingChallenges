
import pytest
from solutions.solution_95 import flatten, TreeNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.right
    return res

@pytest.mark.parametrize("root, expected", [
    (TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))), [1, 2, 3, 4, 5, 6]),
    (None, []),
    (TreeNode(0), [0])
])
def test_flatten(root, expected):
    flatten(root)
    assert to_list(root) == expected
