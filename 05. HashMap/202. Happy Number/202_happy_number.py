class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            result = 0
            for c in str(n):
                result += int(c) * int(c)
            
            n = result
        
        return True