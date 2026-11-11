# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:        
        indexes = []
        nums = []

        curr = head
        counter = 0
        while curr.next.next:
            prev = curr.val
            current = curr.next.val
            nxt = curr.next.next.val

            if (current > prev and current > nxt) or (current < prev and current < nxt):
                indexes.append(counter)
            
            counter += 1
            curr = curr.next

        n = len(indexes)

        if n == 0 or n == 1:
            return [-1, -1]
        
        minDistance = float('inf')
        for i in range(1, n):
            minDistance = min(minDistance, indexes[i] - indexes[i-1])
        maxDistance = indexes[n-1] - indexes[0]

        return [minDistance, maxDistance]
