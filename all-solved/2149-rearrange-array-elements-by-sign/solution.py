class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)

        i = 0
        for n in nums:
            if n >= 0:
                result[i] = n
                i += 2
        
        i = 1
        for n in nums:
            if n < 0:
                result[i] = n
                i += 2
        
        return result
