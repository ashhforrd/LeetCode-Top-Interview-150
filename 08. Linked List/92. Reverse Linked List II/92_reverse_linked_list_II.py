# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        result = ListNode(0, head)

        leftPrev, curr = result, head
        for _ in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return result.next