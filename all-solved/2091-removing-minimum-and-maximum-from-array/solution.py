class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        minFromLeft, maxFromLeft, minFromLeft, minFromRight = 0, 0, 0, 0

        n = len(nums)
        
        for i in range(n):
            if nums[i] == minimum:
                minFromLeft = i + 1
            
            if nums[i] == maximum:
                maxFromLeft = i + 1

        for i in range(n-1, -1, -1):
            if nums[i] == minimum:
                minFromRight = n - i
            
            if nums[i] == maximum:
                maxFromRight = n - i
        
        print(minFromLeft, maxFromLeft)
        print(minFromRight, maxFromRight)

        return min(
            max(minFromLeft, maxFromLeft), 
            max(minFromRight, maxFromRight), 
            min(minFromLeft + maxFromRight, maxFromLeft + minFromRight)
        )
