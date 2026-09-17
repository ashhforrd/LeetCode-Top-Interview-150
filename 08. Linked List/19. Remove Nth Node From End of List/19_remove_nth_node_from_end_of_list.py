# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        prev, curr = result, head

        count = -1
        while curr:
            count += 1
            curr = curr.next
        
        position = count - n

        curr = result
        for i in range(position):
            curr = curr.next
        
        curr.next = curr.next.next

        return result.next