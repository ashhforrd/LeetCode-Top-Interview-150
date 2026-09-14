class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        res, perm = [], []

        def generate(nums, perm):
            if len(perm) == len(nums):
                res.append(perm)
                return
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    generate(nums, perm + [nums[i]])
        
        generate(nums, perm)
        return res