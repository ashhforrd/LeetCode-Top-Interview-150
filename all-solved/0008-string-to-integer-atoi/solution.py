class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = ""

        if s == "":
            return 0

        if s[0] == "-":
            sign = "negative"
            s = s[1:]
        elif s[0] == "+":
            sign = "positive"
            s = s[1:]
        else:
            sign = "positive"

        result = ""
        for c in s:
            if c.isdigit():
                result += c
            else:
                break
        
        if result == "":
            return 0
        
        new_result = int(result)

        if sign == "negative":
            res = -1 * new_result
            if res < -2**31:
                return -2 ** 31
            else:
                return res
        else:
            if new_result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return new_result
