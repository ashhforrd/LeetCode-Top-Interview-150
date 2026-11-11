class Solution:
    def findScore(self, nums: List[int]) -> int:
        # number = collections.defaultdict(list)
        # for i, n in enumerate(nums):
        #     number[n].append(i)
        # number = dict(sorted(number.items()))

        # unmarked = set(range(len(nums)))
        # score = 0

        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))
        
        score = 0
        marked = set()

        while heap:
            n, i = heapq.heappop(heap)

            if i in marked:
                continue
            
            score += n
            marked.add(i)

            if i > 0:
                marked.add(i - 1)
            if i < len(nums) - 1:
                marked.add(i + 1)
        
        return score
