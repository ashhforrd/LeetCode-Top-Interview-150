class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output, heap = [], []

        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        
        for i in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap and heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            
            minimum, _ = heap[0]
            output.append(-minimum)
        
        return output
