# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0, None)
        curr = result

        if not head:
            return None
        
        while head:
            if head.val != val:
                curr.next = head
                curr = curr.next
            head = head.next

        curr.next = head
        
        return result.next
