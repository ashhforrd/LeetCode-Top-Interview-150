class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []
        arr2Set = set(arr2)

        nums = {}
        for n in arr1:
            nums[n] = nums.get(n, 0) + 1
        
        for n in arr2:
            if n in nums:
                for _ in range(nums[n]):
                    res.append(n)
                nums[n] = 0
        
        nums = collections.OrderedDict(sorted(nums.items()))

        for n in nums:
            if nums[n] != 0:
                for _ in range(nums[n]):
                    res.append(n)
                nums[n] = 0
        
        return(res)
