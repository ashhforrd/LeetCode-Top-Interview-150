class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer_one, answer_two =  [], []
        set_one, set_two = set(nums1), set(nums2)

        for n in nums1:
            if n not in set_two:
                answer_one.append(n)
                set_two.add(n)
        
        for n in nums2:
            if n not in set_one:
                answer_two.append(n)
                set_one.add(n)
            
        return [answer_one, answer_two]
