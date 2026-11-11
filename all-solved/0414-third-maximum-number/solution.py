class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        nums = list(nums)

        print(nums)

        heap = []
        for n in nums:
            heapq.heappush(heap, -n)
        
        if len(heap) < 3:
            return -heapq.heappop(heap)
        
        for _ in range(2):
            heapq.heappop(heap)
        return -heapq.heappop(heap)
