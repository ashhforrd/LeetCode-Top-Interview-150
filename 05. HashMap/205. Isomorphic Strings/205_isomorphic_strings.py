class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char = {}

        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = t[i] if t[i] not in char.values() else ""
            
            if t[i] != char[s[i]]:
                return False
        
        return True