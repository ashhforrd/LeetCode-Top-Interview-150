class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        result = "1"

        for _ in range(n-1):
            old = result
            new_result = ""

            j = 0
            while j < len(old):
                num = old[j]
                count = 0
                while j < len(old) and old[j] == num:
                    j += 1
                    count += 1
                
                new_result += str(count)+num
            
            result = new_result
            
        return result
