class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                m = j + 1
                n = len(nums) - 1

                while m < n:
                    total = nums[i] + nums[j] + nums[m] + nums[n]
                    if total == target:
                        if [nums[i], nums[j], nums[m], nums[n]] not in result:
                            result.append([nums[i], nums[j], nums[m], nums[n]])
                        m += 1
                        n -= 1
                    elif total < target:
                        m += 1
                    elif total > target:
                        n -= 1
        
        return result

        # i = 0
        # j = len(nums) // 2 - 1
        # m = len(nums) // 2
        # n = len(nums) - 1

        # sum_first = 0
        # sum_second = 0

        # while i < j and m < n:
        #     sum_first = nums[i] + nums[j]
        #     sum_second = nums[m] + nums[n]

        #     if sum_first + sum_second == target:
        #         result.append([nums[i], nums[j], nums[m], nums[n]])
            
        #     if sum_first < nums[(i+j) // 2]:
        #         i += 1
        #     else:
        #         j -= 1
            
        #     if sum_second < nums[(m+n) // 2]:
        #         m += 1
        #     else:
        #         n -= 1
        
        # return result
