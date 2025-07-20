
import pytest
from solutions.solution_18 import merge_k_lists, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("lists, expected", [
    ([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([None], []),
    ([ListNode(1)], [1]),
    ([ListNode(1), ListNode(0), ListNode(2)], [0, 1, 2]),
    ([ListNode(1, ListNode(2, ListNode(3))), ListNode(4, ListNode(5, ListNode(6))), ListNode(7, ListNode(8, ListNode(9)))], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([ListNode(1, ListNode(10, ListNode(11))), ListNode(2, ListNode(3, ListNode(12))), ListNode(4, ListNode(5, ListNode(6)))], [1, 2, 3, 4, 5, 6, 10, 11, 12]),
    ([ListNode(1), ListNode(1), ListNode(1)], [1, 1, 1]),
    ([ListNode(1, ListNode(2, ListNode(3))), ListNode(1, ListNode(2, ListNode(3)))], [1, 1, 2, 2, 3, 3]),
    ([None, ListNode(1)], [1]),
    ([ListNode(1), None], [1]),
    ([ListNode(1, ListNode(3, ListNode(5))), ListNode(2, ListNode(4, ListNode(6))), ListNode(0, ListNode(7, ListNode(8)))], [0, 1, 2, 3, 4, 5, 6, 7, 8]),
    ([ListNode(-1, ListNode(-2, ListNode(-3))), ListNode(-4, ListNode(-5, ListNode(-6)))], [-6, -5, -4, -3, -2, -1]),
    ([ListNode(10, ListNode(20, ListNode(30))), ListNode(5, ListNode(15, ListNode(25)))], [5, 10, 15, 20, 25, 30]),
    ([ListNode(1, ListNode(1, ListNode(2))), ListNode(1, ListNode(2, ListNode(2)))], [1, 1, 1, 1, 2, 2]),
    ([ListNode(1, ListNode(4, ListNode(5, ListNode(10)))), ListNode(2, ListNode(3, ListNode(6, ListNode(7))))], [1, 2, 3, 4, 5, 6, 7, 10]),
    ([ListNode(1, ListNode(2)), ListNode(3, ListNode(4)), ListNode(5, ListNode(6)), ListNode(7, ListNode(8))], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([ListNode(1)], [1]),
    ([None, None, None], [])
])
def test_merge_k_lists(lists, expected):
    result_node = merge_k_lists(lists)
    assert to_list(result_node) == expected
