class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}

        for c in magazine:
            if c not in char_count:
                char_count[c] = 1
            else:
                char_count[c] += 1
        
        for c in ransomNote:
            if c not in char_count or char_count[c] == 0:
                return False
            
            char_count[c] -= 1
        
        return True