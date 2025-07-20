
import pytest
from solutions.solution_73 import reverse_between, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, left, right, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4, [1, 4, 3, 2, 5]),
    (ListNode(5), 1, 1, [5]),
    (ListNode(1, ListNode(2)), 1, 2, [2, 1]),
    (ListNode(1, ListNode(2, ListNode(3))), 1, 2, [2, 1, 3]),
    (ListNode(1, ListNode(2, ListNode(3))), 2, 3, [1, 3, 2]),
    (ListNode(1, ListNode(2, ListNode(3))), 1, 3, [3, 2, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2, 3, [1, 3, 2, 4]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 1, 4, [4, 3, 2, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 5, [5, 4, 3, 2, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4, [1, 4, 3, 2, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 1, [1, 2, 3, 4, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, 5, [1, 2, 3, 4, 5]),
    (ListNode(1), 1, 1, [1]),
    (None, 1, 1, [])
])
def test_reverse_between(head, left, right, expected):
    result_node = reverse_between(head, left, right)
    assert to_list(result_node) == expected
