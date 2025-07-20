
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
    (TreeNode(0), [0]),
    (TreeNode(1, TreeNode(2)), [1, 2]),
    (TreeNode(1, None, TreeNode(2)), [1, 2]),
    (TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), [1, 2, 4, 3]),
    (TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(5))), [1, 2, 3, 5]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), [1, 2, 4, 3, 5]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5))), [1, 2, 4, 6, 3, 5]),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5, TreeNode(7)))), [1, 2, 4, 3, 5, 7]),
    (TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6))), TreeNode(3, TreeNode(5, TreeNode(7)))), [1, 2, 4, 6, 3, 5, 7]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [4, 2, 1, 3, 6, 5, 7]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), None)), [4, 2, 1, 3, 6, 5]),
    (TreeNode(4, TreeNode(2, TreeNode(1), None), TreeNode(6, TreeNode(5), TreeNode(7))), [4, 2, 1, 6, 5, 7]),
    (TreeNode(4, TreeNode(2, None, TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))), [4, 2, 3, 6, 5, 7]),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), None), [4, 2, 1, 3]),
    (TreeNode(4, None, TreeNode(6, TreeNode(5), TreeNode(7))), [4, 6, 5, 7]),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))))), [1, 2, 3, 4, 5])
])
def test_flatten(root, expected):
    flatten(root)
    assert to_list(root) == expected
