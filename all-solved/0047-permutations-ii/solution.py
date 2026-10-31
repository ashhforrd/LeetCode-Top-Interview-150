class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        result = []
        temp = []
        used_index = []
        
        self.generate(nums, result, temp, used_index)

        return result

    def generate(self, nums, result, temp, used_index):
        if len(temp) == len(nums) and temp not in result:
            result.append(temp)
            
        for i in range(len(nums)):
            if i not in used_index:
                self.generate(nums, result, temp + [nums[i]], used_index + [i])
