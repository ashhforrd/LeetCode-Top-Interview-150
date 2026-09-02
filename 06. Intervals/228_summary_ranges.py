class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        left = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                continue
            else:
                if nums[left] == nums[i]:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[i]))
                left = i + 1
        

        if nums[left] == nums[-1]:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left]) + "->" + str(nums[-1]))
    
        return result