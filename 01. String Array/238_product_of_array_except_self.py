class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        answer = [1 for i in range(n)]

        left_product = 1
        for i in range(1, n):
            left_product *= nums[i-1]
            answer[i] *= left_product
        
        right_product = 1
        for j in range(n-2, -1, -1):
            right_product *= nums[j+1]
            answer[j] *= right_product
        
        return answer