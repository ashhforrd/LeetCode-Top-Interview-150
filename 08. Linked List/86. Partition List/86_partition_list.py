# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        hashNodeLess = {}

        current = head
        count = 0
        while current:
            value = current.val
            if value < x:
                hashNodeLess[count] = value
                count += 1
     
            current = current.next
        
        output = ListNode()
        currOutput = output
        current = head

        for i in range(len(hashNodeLess)):
            currOutput.next = ListNode(hashNodeLess[i])
            currOutput = currOutput.next

        while current:
            if current.val < x:
                current = current.next
            else:
                currOutput.next = ListNode(current.val)
                current = current.next
                currOutput = currOutput.next
        
        return output.next