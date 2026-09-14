class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def generate(nums, start):
            if len(nums) == k:
                result.append(nums)
                return
            
            for i in range(start, n + 1):
                generate(nums + [i], i + 1)

        generate([], 1)
        return result