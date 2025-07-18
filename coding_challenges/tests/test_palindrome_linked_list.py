
import pytest
from solutions.solution_135 import isPalindrome

# Test cases for Palindrome Linked List

# Helper function to create a linked list from a Python list
def create_linked_list(nums):
    head = None
    tail = None
    for num in nums:
        node = ListNode(num)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

# ListNode class (assuming it's defined in solution_135.py or a similar file)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 2, 1], True),
    ([1, 2], False),
    ([1, 0, 1], True),
    ([1, 1, 2, 1], False),
    ([1], True),
    ([], True), #Empty list is a palindrome
    ([1, 2, 3, 2, 1], True),
    ([1, 2, 3, 3, 2, 1], True),
    ([1, 2, 3, 4, 5], False),
    ([1, 2, 3, 4, 4, 3, 2, 1], True),
    ([1, 0, 0, 1], True),
    ([1, 0, 0, 0, 1], True),
    ([-1, 0, 0, -1], True),
    ([-1, 0, 1, 0, -1], True),
    ([123, 231], False), #Handles multi-digit numbers correctly
    ([121, 121], False), #Handles multi-digit numbers correctly
    ([1, -1], True),
    ([0, 0], True),
    ([0], True),
    ([-1,-1], True),
    ([121], True), #Single node palindrome
    ([9,9],True),
    ([-9,-9], True),
    ([100000001],True),
    ([1,2,3,4,3,2,1], True),
    ([1,2,3,4,5,4,3,2,1], True),
    ([1,2,3,4,5,6,7,8,9], False),
    ([9,8,7,6,5,4,3,2,1], False),
    ([1,0,1], True),
    ([1,2,1], True),
    ([1,0,0,1], True),
    ([1, 0, 1, 0, 1], True), # longer alternating
    ([1, 2, 3, 4], False),
    ([4, 3, 2, 1], False),
    ([1,2, 2, 1], True),
    ([1, 1, 1, 1], True),
    ([1, 1, 1, 1, 1], True),
    ([1,1,2,2,1,1], True),
    ([1,2,3,3,2,1], True),
    ([1,2,3,2,1],True),
    ([1,2,3,4,3,2,1], True),
    ([1, 2, 3, 4, 4, 3, 2, 1], True),
    ([1, 2, 2, 1], True),
    ([0,0,0], True),
    ([-1,0,1,0,-1], True),
    ([1,-1], True),
    ([10001],True),
    ([100001], True),
    ([1000001],True),
    ([10000001], True),
])
def test_palindrome_linked_list(input_list, expected):
    head = create_linked_list(input_list)
    assert isPalindrome(head) == expected

