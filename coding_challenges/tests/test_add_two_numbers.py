
import pytest
from solutions.solution_2 import add_two_numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("l1, l2, expected", [
    (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))), [7, 0, 8]),
    (ListNode(0), ListNode(0), [0]),
    (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), [8, 9, 9, 9, 0, 0, 0, 1]),
    (ListNode(1), ListNode(9, ListNode(9)), [0, 0, 1]),
    (ListNode(1, ListNode(8)), ListNode(0), [1, 8]),
    (ListNode(5), ListNode(5), [0, 1]),
    (ListNode(2, ListNode(4)), ListNode(5, ListNode(6, ListNode(4))), [7, 0, 5]),
    (ListNode(1), ListNode(9), [0, 1]),
    (ListNode(9), ListNode(1), [0, 1]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6))), [5, 7, 9]),
    (ListNode(1, ListNode(8)), ListNode(0), [1, 8]),
    (ListNode(0), ListNode(1, ListNode(8)), [1, 8]),
    (ListNode(1), ListNode(9, ListNode(9, ListNode(9))), [0, 0, 0, 1]),
    (ListNode(9, ListNode(9, ListNode(9))), ListNode(1), [0, 0, 0, 1]),
    (ListNode(1, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))), ListNode(5, ListNode(6, ListNode(4))), [6, 6, 4, 0, 1]),
    (ListNode(0), ListNode(0, ListNode(0, ListNode(1))), [0, 0, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(0))))), [7, 9, 1, 4, 6]),
    (ListNode(9, ListNode(8, ListNode(7))), ListNode(1, ListNode(2, ListNode(3))), [0, 1, 1, 1]),
    (ListNode(1), ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))), [0, 0, 0, 0, 0, 1]),
    (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))), ListNode(1), [0, 0, 0, 0, 0, 1]),
    (ListNode(1, ListNode(0, ListNode(0))), ListNode(9, ListNode(9, ListNode(9))), [0, 0, 0, 1]),
    (ListNode(9, ListNode(9, ListNode(9))), ListNode(1, ListNode(0, ListNode(0))), [0, 0, 0, 1]),
    (ListNode(6, ListNode(6, ListNode(6))), ListNode(4, ListNode(4, ListNode(4))), [0, 1, 1, 1]),
    (ListNode(3, ListNode(7)), ListNode(9, ListNode(2)), [2, 0, 1]),
    (ListNode(1, ListNode(8, ListNode(3))), ListNode(7, ListNode(1)), [8, 9, 3]),
    (ListNode(9, ListNode(9)), ListNode(1), [0, 0, 1]),
    (ListNode(1), ListNode(9, ListNode(9)), [0, 0, 1]),
    (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))), [7, 0, 8]),
    (ListNode(0), ListNode(0), [0]),
    (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))), [8, 9, 9, 9, 0, 0, 0, 1]),
    (ListNode(1), ListNode(1), [2]),
    (ListNode(1, ListNode(2)), ListNode(1, ListNode(2)), [2, 4]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(2, ListNode(3))), [2, 4, 6]),
    (ListNode(9, ListNode(9)), ListNode(9, ListNode(9)), [8, 9, 1]),
    (ListNode(1, ListNode(0, ListNode(1))), ListNode(9, ListNode(0, ListNode(9))), [0, 1, 0, 1]),
    (ListNode(1), None, [1]),
    (None, ListNode(1), [1]),
    (None, None, []),
    (ListNode(0), ListNode(1), [1]),
    (ListNode(1), ListNode(0), [1]),
    (ListNode(9), ListNode(9), [8, 1]),
    (ListNode(9, ListNode(8)), ListNode(1, ListNode(2)), [0, 1, 1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), None, [1, 2, 3, 4, 5]),
    (None, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [1, 2, 3, 4, 5]),
    (ListNode(1, ListNode(1, ListNode(1))), ListNode(9, ListNode(9, ListNode(9))), [0, 1, 1, 1]),
    (ListNode(9, ListNode(9, ListNode(9))), ListNode(1, ListNode(1, ListNode(1))), [0, 1, 1, 1]),
    (ListNode(5, ListNode(5, ListNode(5))), ListNode(5, ListNode(5, ListNode(5))), [0, 1, 1, 1]),
    (ListNode(1, ListNode(2, ListNode(3))), ListNode(9, ListNode(8, ListNode(7))), [0, 1, 1, 1]),
    (ListNode(9, ListNode(8, ListNode(7))), ListNode(1, ListNode(2, ListNode(3))), [0, 1, 1, 1])
])
def test_add_two_numbers(l1, l2, expected):
    result_node = add_two_numbers(l1, l2)
    assert to_list(result_node) == expected
