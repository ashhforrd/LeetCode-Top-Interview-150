class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        result = []
        temp = []
        
        self.generate(nums, result, temp)

        return result

    def generate(self, nums, result, temp):
        if len(temp) == len(nums):
            result.append(temp)
            
        for i in range(len(nums)):
            if nums[i] not in temp:
                self.generate(nums, result, temp + [nums[i]])
