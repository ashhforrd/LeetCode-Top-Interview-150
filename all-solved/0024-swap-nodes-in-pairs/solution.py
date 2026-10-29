# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result.next = head
        temp = result

        while temp.next is not None and temp.next.next is not None:
            node1 = temp.next
            node2 = temp.next.next
            next_pair = node2.next

            temp.next = node2
            node2.next = node1
            node1.next = next_pair

            temp = temp.next.next
        
        return result.next
