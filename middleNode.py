class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, slow and fast, both pointing to the head of the linked list.
        slow = head
        fast = head

        # Traverse the linked list using the slow and fast pointers.
        # The fast pointer moves two steps at a time while the slow pointer moves one step at a time.
        # This way, when the fast pointer reaches the end of the linked list, the slow pointer will be at the middle node.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Return the node pointed to by the slow pointer, which represents the middle of the linked list.
        return slow
