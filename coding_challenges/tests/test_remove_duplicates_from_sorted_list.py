import pytest
from solutions.solution_59 import delete_duplicates, ListNode

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

@pytest.mark.parametrize("head, expected", [
    (ListNode(1, ListNode(1, ListNode(2))), [1, 2]),
    (ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))), [1, 2, 3]),
    (None, []),
    (ListNode(1, ListNode(1, ListNode(1))), [1]),
    (ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(3)))))), [1, 2, 3]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1))))), [1]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [1, 2, 3, 4, 5]),
    (ListNode(-1, ListNode(0, ListNode(0, ListNode(0, ListNode(1, ListNode(1, ListNode(2))))))), [-1, 0, 1, 2]),
    (ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))), [1, 2, 3, 4]),
    (ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(4, ListNode(4))))))))))), [1, 2, 3, 4]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(3))))))))), [1, 2, 3]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(2, ListNode(3)))))), [1, 2, 3, 1, 2, 3]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(2)))))))), [1, 2]),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))))), [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1)))))))))), [1]),
    (ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(1, ListNode(2)))))))))), [1, 2]),
    (ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2)))))))))), [1, 2])
])
def test_delete_duplicates(head, expected):
    result_node = delete_duplicates(head)
    assert to_list(result_node) == expected