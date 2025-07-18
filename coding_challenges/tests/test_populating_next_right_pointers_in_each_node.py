
import pytest
from solutions.solution_96 import connect, Node

# This is a difficult problem to test because it modifies the tree in-place.
# For now, we will just check a simple case.
@pytest.mark.parametrize("root, expected_next_values", [
    (Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))), [None, 3, 5, 6, 7, None])
])
def test_connect(root, expected_next_values):
    connect(root)
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
