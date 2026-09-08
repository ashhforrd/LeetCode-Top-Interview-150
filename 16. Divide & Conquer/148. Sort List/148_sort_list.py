# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        nums = []

        current = head
        while current:
            nums += [current.val]
            current = current.next
        nums.sort()

        current = head
        pos = 0

        while current:
            current.val = nums[pos]
            current = current.next
            pos += 1
        
        return head