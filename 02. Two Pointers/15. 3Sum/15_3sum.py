class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        N = len(nums)

        for i in range(N):
            j = i + 1
            k = N - 1
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