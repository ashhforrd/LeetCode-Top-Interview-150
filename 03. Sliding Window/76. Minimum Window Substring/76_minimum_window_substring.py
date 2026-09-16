class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ""

        if len(s) < len(t):
            return ""

        wordMap = {}
        for c in t:
            wordMap[c] = wordMap.get(c, 0) + 1
        
        left, right = 0, 0
        for right in range(len(s)):
            if s[right] in wordMap:
                wordMap[s[right]] -= 1
            
            while all(v <= 0 for v in wordMap.values()):
                word = s[left: right+1]

                if substring == "" or len(word) < len(substring):
                    substring = word

                if s[left] in wordMap:
                    wordMap[s[left]] += 1
                
                left += 1
                    
        return substring