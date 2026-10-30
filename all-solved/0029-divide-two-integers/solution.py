class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dv = abs(divisor)

        result = 0

        while dv <= d:
            temp = dv
            multiplier = 1
            while temp <= d:
                d -= temp
                result += multiplier
                multiplier += multiplier
                temp += temp
        
        if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0):
            result = -1 * result
        
        return min(2**31-1, max(-2**31, result))
