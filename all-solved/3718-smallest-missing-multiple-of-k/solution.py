class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numSet = set(nums)
        number = k
        while number <= 100:
            if number not in numSet:
                return number
            number += k
        return number
