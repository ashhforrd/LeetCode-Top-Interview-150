# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        remaining = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            value = val1 + val2 + remaining
            remaining = 0

            remaining = value // 10
            value = value % 10

            current.next = ListNode(value)
            current = current.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if remaining != 0:
            current.next = ListNode(remaining)
            current = current.next
        
        return result.next