# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      # Initialize variables for the first linked list
      start_l1 = l1.val
      current = l1.next

      # Initialize variables for the second linked list
      start_l2 = l2.val
      current_l2 = l2.next

      # Compute the value of the first linked list by multiplying each digit by the appropriate power of 10
      iteration = 1
      while current is not None:
          start_l1 += current.val * 10 ** iteration
          current = current.next
          iteration += 1

      # Compute the value of the second linked list by multiplying each digit by the appropriate power of 10
      iteration = 1
      while current_l2 is not None:
          start_l2 += current_l2.val * 10 ** iteration
          current_l2 = current_l2.next
          iteration += 1

      # Compute the final sum
      fin = start_l1 + start_l2

      # Create a new linked list to store the digits of the final sum
      f1 = ListNode(fin % 10, ListNode(fin))
      prev = None

      # Convert the final sum to individual digits and create linked list nodes
      for i in str(fin):
          f1 = ListNode(int(i))
          f1.next = prev
          prev = f1

      # Return the head of the final linked list
      return f1
