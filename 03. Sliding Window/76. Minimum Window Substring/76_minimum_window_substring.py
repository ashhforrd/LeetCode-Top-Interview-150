class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ""
        left, right = 0, 0

        if len(s) < len(t):
            return ""

        tMap = {}
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        
        while right < len(s):
            if s[right] in tMap:
                tMap[s[right]] -= 1
            
            while all(c <= 0 for c in tMap.values()):
                temp = s[left: right + 1]
                if output == "" or len(temp) < len(output): output = temp
                if s[left] in tMap: tMap[s[left]] += 1
                left += 1

            right += 1
        
        return output