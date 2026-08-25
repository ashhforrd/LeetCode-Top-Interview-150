class Solution:
    def intToRoman(self, num: int) -> str:
        thousand = (num // 1000) 
        num = num % 1000

        hundred = (num // 100)
        num = num % 100
        
        tens = (num // 10)
        num = num % 10

        # case 3749
        # thousans = 3000
        # hundred = 700
        # tens = 40
        # singles = 9

        # case 58
        # tens = 5
        # singles = 8
        
        # case 1
        # singles = 1

        result = ""
        result += "M" * thousand
        
        if hundred == 4:
            result += "CD"
        elif hundred == 9:
            result += "CM"
        elif hundred == 5:
            result += "D"
        elif hundred < 4:
            result += "C" * hundred
        elif hundred < 9 and hundred > 5:
            result += "D"
            result += "C" * (hundred - 5)

        if tens == 4:
            result += "XL"
        elif tens == 9:
            result += "XC"
        elif tens == 5:
            result += "L"
        elif tens < 4:
            result += "X" * tens
        elif tens < 9 and tens > 5:
            result += "L"
            result += "X" * (tens - 5)
        
        if num == 4:
            result += "IV"
        elif num == 9:
            result += "IX"
        elif num == 5:
            result += "V"
        elif num < 4:
            result += "I" * num
        elif num < 9 and num > 5:
            result += "V"
            result += "I" * (num - 5)
        
        return result