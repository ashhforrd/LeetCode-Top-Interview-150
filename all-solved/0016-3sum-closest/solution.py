class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nearest = 100000

        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(nearest - target):
                    nearest = total
                
                if total < target:
                    j += 1
                else:
                    k -= 1      
        
        return nearest
