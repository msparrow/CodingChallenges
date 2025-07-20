
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)  # Create a dummy head node to simplify the logic
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:  # Continue until both lists are processed and carry is 0

        val1 = l1.val if l1 else 0  # Handle cases where one list is shorter
        val2 = l2.val if l2 else 0

        sum_digits = val1 + val2 + carry
        carry = sum_digits // 10  # Integer division to get the carry
        digit = sum_digits % 10    # Modulo operation to get the digit

        current.next = ListNode(digit)  # Create a new node with the digit
        current = current.next       # Move to the next node

        l1 = l1.next if l1 else None  # Move to the next node in l1 or set to None
        l2 = l2.next if l2 else None

    return dummy_head.next  # Return the next node after the dummy head
