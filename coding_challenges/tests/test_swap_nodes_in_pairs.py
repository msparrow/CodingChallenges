
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
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [2, 1, 4, 3, 5]),
    (ListNode(1, ListNode(2)), [2, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), [2, 1, 4, 3, 6, 5]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))), [2, 1, 4, 3, 6, 5, 7]),
    (ListNode(0, ListNode(1)), [1, 0]),
    (ListNode(-1, ListNode(0)), [0, -1]),
    (ListNode(10, ListNode(20, ListNode(30))), [20, 10, 30]),
    (ListNode(1, ListNode(1, ListNode(2, ListNode(2)))), [1, 1, 2, 2]),
    (ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), [2, 1, 1, 2]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))), [2, 1, 3, 3, 1, 2]),
    (ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))), [4, 5, 2, 3, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8)))))))), [2, 1, 4, 3, 6, 5, 8, 7]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9))))))))), [2, 1, 4, 3, 6, 5, 8, 7, 9]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(1)))), [1, 1, 1, 1]),
    (ListNode(0, ListNode(0, ListNode(0, ListNode(0)))), [0, 0, 0, 0]),
    (ListNode(-1, ListNode(-2, ListNode(-3, ListNode(-4)))), [-2, -1, -4, -3])
])
def test_swap_pairs(head, expected):
    result_node = swap_pairs(head)
    assert to_list(result_node) == expected
