class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ""
        
        if len(s) < len(t):
            return substring
        
        char = {}
        for c in t:
            char[c] = char.get(c, 0) + 1
        
        left = 0
        for right in range(len(s)):
            if s[right] in char:
                char[s[right]] -= 1
            
            while all(v <= 0 for v in char.values()):
                word = s[left: right + 1]

                if substring == "" or len(word) < len(substring):
                    substring = word
                
                if s[left] in char:
                    char[s[left]] += 1
                
                left += 1
        
        return substring