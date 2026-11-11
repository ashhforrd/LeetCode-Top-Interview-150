class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        maps = {}

        for num in nums2:
            while stack and num > stack[-1]:
                maps[stack.pop()] = num

            stack.append(num)
        
        res = []
        for num in nums1:
            if num in maps:
                res.append(maps[num])
            else:
                res.append(-1)
        
        return res
