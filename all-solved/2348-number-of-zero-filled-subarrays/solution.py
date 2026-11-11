class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        def triangular(n):
            return n * (n + 1) // 2
        
        res = 0
        length = 0
        for n in nums:
            if n == 0:
                length += 1
            else:
                res += triangular(length)
                length = 0
        
        if length:
            res += triangular(length)

        return res
