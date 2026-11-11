class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        values = Counter(nums)

        res = 0

        for key in values:
            if values[key] == 1:
                res += key
        
        return res
