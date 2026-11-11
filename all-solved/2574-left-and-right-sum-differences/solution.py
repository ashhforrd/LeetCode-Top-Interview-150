class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum, rightSum = [0] * n, [0] * n

        currSum = 0
        for i in range(1, n):
            currSum += nums[i - 1]
            leftSum[i] = currSum
        
        currSum = 0
        for j in reversed(range(n - 1)):
            currSum += nums[j + 1]
            rightSum[j] = currSum

        answer = []
        for k in range(n):
            answer.append(abs(leftSum[k] - rightSum[k]))

        return answer
