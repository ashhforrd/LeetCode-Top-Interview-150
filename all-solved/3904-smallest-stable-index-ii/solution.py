class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefMax, suffMin = [], []

        maxNum = nums[0]
        for i in range(len(nums)):
            maxNum = max(maxNum, nums[i])
            prefMax.append(maxNum)
        
        minNum = nums[len(nums) - 1]
        for j in range(len(nums) - 1, -1, -1):
            minNum = min(minNum, nums[j])
            suffMin.append(minNum)
        
        suffMin.reverse()

        for r in range(len(nums)):
            instability = prefMax[r] - suffMin[r]

            if instability <= k:
                return r

        return -1
