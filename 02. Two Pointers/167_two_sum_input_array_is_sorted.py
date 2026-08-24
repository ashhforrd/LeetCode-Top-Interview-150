class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sums = numbers[left] + numbers[right]

            if sums > target:
                right -= 1
            elif sums < target:
                left += 1
            elif sums == target:
                return [left + 1, right + 1]