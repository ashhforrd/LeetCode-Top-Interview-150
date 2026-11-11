class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            res = 0
            for c in str(num):
                res += int(c)
            
            num = res
        
        return int(num)
