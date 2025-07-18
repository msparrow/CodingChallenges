import pytest
from solutions.solution_60 import delete_duplicates2, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, expected", [
    (ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))), [1, 2, 5]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))), [2, 3]),
    (None, []),
    (ListNode(1, ListNode(1)), [])
])
def test_delete_duplicates2(head, expected):
    result_node = delete_duplicates2(head)
    assert to_list(result_node) == expected