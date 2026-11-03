class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.generate(result, nums, 0, [])
        return result

    def generate(self, result, nums, start, temp):
        result.append(temp)

        if len(temp) == len(nums):
            return

        for i in range(start, len(nums)):
            self.generate(result, nums, i + 1, temp + [nums[i]])
