class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        currSum = 0
        prefSum = { 0: 1 }

        for n in nums:
            currSum += n
            diff = currSum - k

            total += prefSum.get(diff, 0)
            prefSum[currSum] = 1 + prefSum.get(currSum, 0)
        
        return total
