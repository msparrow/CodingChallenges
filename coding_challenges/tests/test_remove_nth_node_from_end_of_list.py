
import pytest
from solutions.solution_14 import remove_nth_from_end, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, n, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, [1, 2, 3, 5]),
    (ListNode(1), 1, []),
    (ListNode(1, ListNode(2)), 1, [1]),
    (ListNode(1, ListNode(2)), 2, [2]),
    (ListNode(1, ListNode(2, ListNode(3))), 3, [2, 3]),
    (ListNode(1, ListNode(2, ListNode(3))), 1, [1, 2]),
    (ListNode(1, ListNode(2, ListNode(3))), 2, [1, 3]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))))))), 5, [1, 2, 3, 4, 5, 7, 8, 9, 10]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 5, [2, 3, 4, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, [1, 2, 3, 4]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3, [1, 2, 4, 5]),
    (ListNode(1), 1, []),
    (ListNode(1, ListNode(2)), 2, [2]),
    (ListNode(1, ListNode(2)), 1, [1]),
    (ListNode(1, ListNode(2, ListNode(3))), 1, [1, 2]),
    (ListNode(1, ListNode(2, ListNode(3))), 2, [1, 3]),
    (ListNode(1, ListNode(2, ListNode(3))), 3, [2, 3]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 2, [1, 2, 4]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 4, [2, 3, 4])
])
def test_remove_nth_from_end(head, n, expected):
    result_node = remove_nth_from_end(head, n)
    assert to_list(result_node) == expected
