class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                
                if total < 0:
                    j += 1
                else:
                    k -= 1
        
        result = list(set(tuple(x) for x in result))
        result = [list(x) for x in result]
        return result