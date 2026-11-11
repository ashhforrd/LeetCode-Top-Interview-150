class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            remain = abs(first - second)

            heapq.heappush(heap, -remain)
        
        if heap:
            return -heap[0]
        else:
            return 0
