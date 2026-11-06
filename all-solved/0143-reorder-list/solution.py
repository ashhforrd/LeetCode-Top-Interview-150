# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        while curr.next:
            nxt = curr.next

            last = stack.pop()
            stack[-1].next = None

            if nxt == last:
                curr.next = last
                break

            last.next = nxt
            curr.next = last
            curr = nxt
