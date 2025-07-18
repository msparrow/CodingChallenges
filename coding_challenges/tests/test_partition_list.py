
import pytest
from solutions.solution_67 import partition, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, x, expected", [
    (ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3, [1, 2, 2, 4, 3, 5]),
    (ListNode(2, ListNode(1)), 2, [1, 2]),
    (ListNode(1), 0, [1]),
    (ListNode(1), 2, [1])
])
def test_partition(head, x, expected):
    result_node = partition(head, x)
    assert to_list(result_node) == expected
