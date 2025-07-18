
import pytest
from solutions.solution_20 import reverse_k_group, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, k, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, [2, 1, 4, 3, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3, [3, 2, 1, 4, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, [1, 2, 3, 4, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, [5, 4, 3, 2, 1]),
    (ListNode(1), 1, [1])
])
def test_reverse_k_group(head, k, expected):
    result_node = reverse_k_group(head, k)
    assert to_list(result_node) == expected
