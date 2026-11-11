class Solution:
    def findLucky(self, arr: list[int]) -> int:
        nums = {}
        for n in arr:
            nums[n] = nums.get(n, 0) + 1
        
        res = -1
        for n in nums:
            if n == nums[n]:
                res = max(res, n)
        
        return res
