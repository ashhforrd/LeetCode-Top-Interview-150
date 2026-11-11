# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        maximum = 0

        numbers = []
        
        curr = head
        while curr:
            numbers.append(curr.val)
            curr = curr.next
        
        for i in range(len(numbers) // 2):
            maximum = max(maximum, numbers[i] + numbers[len(numbers) - 1 - i])
        
        return maximum
