
import pytest
from solutions.solution_125 import hasCycle, ListNode

# Test cases for Linked List Cycle

# Helper function to create a linked list from a list of numbers
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

# Helper function to create a cycle in a linked list
def create_cycle(head, pos):
    if pos == -1:
        return head
    temp = head
    tail = head
    count = 0
    while count < pos:
        tail = tail.next
        count += 1
    while temp.next:
        temp = temp.next
    temp.next = tail
    return head

# Test cases with different list sizes and cycle positions
test_cases = [
    ([3, 2, 0, -4], 1, True),  # Cycle at 1
    ([1, 2], 0, True), # Cycle at 0
    ([1], -1, False),  # No cycle
    ([1, 2, 3, 4, 5], 2, True),  # Cycle at 2
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, True),  # Larger list, cycle at 5
    ([], -1, False),  # Empty list
    ([1,2,3,4,5], -1, False), # No cycle
    ([1,2],1, True), # Cycle at 1
    ([1,2,2,2,2], 1, True), #Cycle at 1, repeated values
    ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 10, True), # Larger list, cycle at 10

]

# additional test cases for edge cases and various lengths of lists

test_cases.extend([
    ([i for i in range(100)], 50, True), # Large list with cycle in the middle
    ([i for i in range(100)], 99, True), # Large list with cycle at the end
    ([i for i in range(100)], -1, False), # Large list without cycle
    ([1,2,3,4,5,6,7,8,9,10], -1, False),
    ([1,2,3,4,5,6,7,8,9,10], 9, True),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5, True),  # Decreasing numbers
    ([1, 1, 1, 1, 1], 0, True),  # All same numbers
    ([1, 2, 3, 4, 5, 1], 5, True), # Cycle to the beginning
    ([1,2,3,4,5,6,7,8,9,10, 12, 14], 2, True), # Non consecutive cycle


])

#Pytest functions to run tests
@pytest.mark.parametrize("nums, pos, expected", test_cases)
def test_hasCycle(nums, pos, expected):
    head = create_linked_list(nums)
    head = create_cycle(head, pos)
    assert hasCycle(head) == expected
