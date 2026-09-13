# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head

        nodeMap = {}
        counter = 1
        while current:
            nodeMap[counter] = current.val
            counter += 1
            current = current.next
        
        output = ListNode()
        pointer = output

        i = 1
        while i <= len(nodeMap):
            if i == left:
                for j in range(right, left-1, -1):
                    pointer.next = ListNode(nodeMap[j])
                    pointer = pointer.next
                i = right + 1
            else:
                pointer.next = ListNode(nodeMap[i])
                pointer = pointer.next
                i += 1
                    
        return output.next


        