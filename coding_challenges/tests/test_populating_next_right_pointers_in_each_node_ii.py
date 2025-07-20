
import pytest
from solutions.solution_97 import connect2, Node

# This is a difficult problem to test because it modifies the tree in-place.
# For now, we will just check a simple case.
@pytest.mark.parametrize("root, expected_next_values", [
    (Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7))), [None, 3, 5, 7, None, None]),
    (None, []),
    (Node(1), [None]),
    (Node(1, Node(2), Node(3)), [None, 3, None]),
    (Node(1, Node(2, Node(4)), Node(3, None, Node(6))), [None, 3, 6, None]),
    (Node(1, Node(2, Node(4), Node(5)), Node(3)), [None, 3, 5, None]),
    (Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7))), [None, 3, 5, 7, None, None]),
    (Node(1, Node(2, Node(4, Node(8)), Node(5, None, Node(9))), Node(3, Node(6, None, Node(10)), Node(7, None, Node(11)))), [None, 3, 5, 6, 7, 9, 10, 11, None]),
    (Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5, Node(10), Node(11))), Node(3, Node(6, Node(12), Node(13)), Node(7, Node(14), Node(15)))), [None, 3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, None])
])
def test_connect2(root, expected_next_values):
    connect2(root)
    # This is a shallow check. A deep check would be more robust.
    # We are checking the 'next' pointers of the nodes in level order.
    result_next_values = []
    q = [root]
    while q:
        node = q.pop(0)
        if node:
            result_next_values.append(node.next.val if node.next else None)
            q.append(node.left)
            q.append(node.right)
    assert result_next_values == expected_next_values
