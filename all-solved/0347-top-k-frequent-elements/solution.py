class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numbers = Counter(nums)

        heap = [(-freq, num) for num, freq in numbers.items()]
        heapq.heapify(heap)
        
        res = []
        for _ in range(k):
            _, n = heapq.heappop(heap)
            res.append(n)
        
        return res
