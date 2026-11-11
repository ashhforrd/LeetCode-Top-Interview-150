class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        dp = {0}
        total = total // 2

        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                if t + nums[i] <= total:
                    if t + nums[i] == total:
                        return True
                    nextDP.add(t + nums[i])
            dp.update(nextDP)

        return True if total in dp else False
