class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char = {}

        if len(magazine) < len(ransomNote):
            return False

        for c in magazine:
            char[c] = char.get(c, 0) + 1
        
        for c in ransomNote:
            if c not in char or char[c] == 0:
                return False  
            char[c] -= 1
        
        return True