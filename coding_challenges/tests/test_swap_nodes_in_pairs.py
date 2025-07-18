
import pytest
from solutions.solution_19 import swap_pairs, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [2, 1, 4, 3]),
    (None, []),
    (ListNode(1), [1]),
    (ListNode(1, ListNode(2, ListNode(3))), [2, 1, 3]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [2, 1, 4, 3, 5])
])
def test_swap_pairs(head, expected):
    result_node = swap_pairs(head)
    assert to_list(result_node) == expected
