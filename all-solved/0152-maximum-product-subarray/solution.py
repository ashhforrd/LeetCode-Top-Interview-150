class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        maxprod, minprod = 1, 1

        for n in nums:
            if n == 0:
                maxprod, minprod = 1, 1
                continue
            
            tmp = maxprod * n
            maxprod = max(n, maxprod * n, minprod * n)
            minprod = min(n, minprod * n, tmp)
            res = max(res, maxprod)
        
        return(res)
