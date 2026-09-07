class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if (len(s) == 1) :return romans[s[0]]
        total = 0
        prev = romans[s[0]]

        for char in s:
            ch = romans[char]
            
            if ch <= prev:
                total += ch
            else: # ch > prev
                total = total - prev + ch - prev
            
            prev = ch
                
        return total
            
