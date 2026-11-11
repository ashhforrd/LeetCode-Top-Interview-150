class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # nums.sort()
        # total = sum(nums)
        # middle = total // len(nums)

        # diff = float('inf')
        # toEqual = 0
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2

        #     subs = nums[mid] - middle

        #     if subs <= diff:
        #         diff = subs
        #         toEqual = nums[mid]
        #         left += 1
        #     else:
        #         right -= 1
        
        # total = 0
        # for n in nums:
        #     total += abs(n - toEqual)
        
        # return total

        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(x - mid) for x in nums)
