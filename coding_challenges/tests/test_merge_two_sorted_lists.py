
import pytest
from solutions.solution_16 import merge_two_lists, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("list1, list2, expected", [
    (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))), [1, 1, 2, 3, 4, 4]),
    (None, None, []),
    (None, ListNode(0), [0]),
    (ListNode(1), None, [1]),
    (ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6))), [1, 2, 3, 4, 5, 6]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6))), [1, 2, 3, 4, 5, 6]),
    (ListNode(4, ListNode(5, ListNode(6))), ListNode(1, ListNode(2, ListNode(3))), [1, 2, 3, 4, 5, 6]),
    (ListNode(1), ListNode(2), [1, 2]),
    (ListNode(2), ListNode(1), [1, 2]),
    (ListNode(1, ListNode(1, ListNode(1))), ListNode(1, ListNode(1, ListNode(1)))), [1, 1, 1, 1, 1, 1]),
    (ListNode(-1, ListNode(0, ListNode(1))), ListNode(-2, ListNode(2, ListNode(3)))), [-2, -1, 0, 1, 2, 3]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(2, ListNode(3)))), [1, 1, 2, 2, 3, 3]),
    (ListNode(1, ListNode(3, ListNode(5, ListNode(7)))), ListNode(2, ListNode(4, ListNode(6, ListNode(8))))), [1, 2, 3, 4, 5, 6, 7, 8]),
    (ListNode(1, ListNode(10, ListNode(20))), ListNode(5, ListNode(15, ListNode(25)))), [1, 5, 10, 15, 20, 25]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10)))))), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    (ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))), ListNode(1, ListNode(2, ListNode(2, ListNode(3))))), [1, 1, 1, 2, 2, 2, 3, 3]),
    (ListNode(1), ListNode(1), [1, 1]),
    (ListNode(1, ListNode(2)), ListNode(1, ListNode(2))), [1, 1, 2, 2]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(2, ListNode(3)))), [1, 1, 2, 2, 3, 3])
])
def test_merge_two_lists(list1, list2, expected):
    result_node = merge_two_lists(list1, list2)
    assert to_list(result_node) == expected
