class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitalHeap, profitHeap = [], []

        for i in range(len(profits)):
            heapq.heappush(capitalHeap, (capital[i], profits[i]))
        
        for _ in range(k):
            while capitalHeap and capitalHeap[0][0] <= w:
                c, p = heapq.heappop(capitalHeap)
                heapq.heappush(profitHeap, -p)
            
            if not profitHeap:
                break
            
            w += -heapq.heappop(profitHeap)
        
        return w