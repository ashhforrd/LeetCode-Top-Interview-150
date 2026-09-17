# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        valueMap = {}

        output = ListNode()
        current = output

        while head:
            if head.val not in valueMap:
                valueMap[head.val] = 1
            else:
                valueMap[head.val] += 1
            head = head.next
                
        for key in valueMap:
            if valueMap[key] == 1:
                current.next = ListNode(key)
                current = current.next
        
        return output.next