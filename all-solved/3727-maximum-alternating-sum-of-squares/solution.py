class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        numbers = []
        for n in nums:
            numbers.append(abs(n))
        numbers.sort()

        left, right = 0, len(nums) - 1

        order = [] 
        while left < right:
            order.append(numbers[right])
            order.append(numbers[left])
        
            right -= 1
            left += 1
        
        if len(nums) % 2 == 1:
            order.append(numbers[right])
        
        res = 0
        sign = "+"
        for n in order:
            if sign == "+":
                res += (n ** 2)
                sign = "-"
            elif sign == "-":
                res -= (n ** 2)
                sign = "+"
                    
        return res
