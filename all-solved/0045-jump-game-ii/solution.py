class Solution:
    def jump(self, nums: List[int]) -> int:
        # totalJump = 0
        # i = 0

        # while i < len(nums) - 1:
        #     numOfJump = nums[i]

        #     if numOfJump + i >= len(nums) - 1:
        #         return totalJump + 1

        #     best = 0
        #     bestValue = 0
        #     for j in range(i+1, min(len(nums), i + nums[i] + 1)):
        #         if j + nums[j] > bestValue:
        #             best = j
        #             bestValue = j + nums[j]

        #     i = best
        #     totalJump += 1

        # return totalJump

        jump = 0
        currentEnd = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                currentEnd = farthest
                jump += 1
        
        return jump
