class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        leftHeap, rightHeap = [], []
        left, right = 0, len(costs) - 1
        for i in range(candidates):
            heapq.heappush(leftHeap, costs[i])
            left += 1

        for j in range(len(costs) - 1, max(left - 1, len(costs) - candidates - 1), - 1):
            heapq.heappush(rightHeap, costs[j])
            right -= 1
        
        total = 0
        for _ in range(k):
            leftMin = leftHeap[0] if leftHeap else float('inf')            
            rightMin = rightHeap[0] if rightHeap else float('inf')

            if leftMin <= rightMin:
                total += heapq.heappop(leftHeap)
                if left <= right:
                    heapq.heappush(leftHeap, costs[left])
                    left += 1
            else:
                total += heapq.heappop(rightHeap)
                if left <= right:
                    heapq.heappush(rightHeap, costs[right])
                    right -= 1
        
        return total
