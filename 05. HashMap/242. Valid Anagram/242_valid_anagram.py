class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}

        if len(s) != len(t):
            return False

        for c in s:
            char[c] = char.get(c, 0) + 1
        
        for c in t:
            if c not in char:
                return False
            
            if char[c] == 0:
                return False

            char[c] -= 1

        return True