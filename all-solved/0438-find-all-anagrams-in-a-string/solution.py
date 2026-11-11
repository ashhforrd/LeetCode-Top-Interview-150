class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []

        char = {}
        for c in p:
            char[c] = char.get(c, 0) + 1

        charMap = char.copy()

        left = 0
        for right in range(len(s)):
            if s[right] in charMap:
                if charMap[s[right]] <= 0:
                    while charMap[s[right]] <= 0:
                        charMap[s[left]] += 1
                        left += 1
                    charMap[s[right]] -= 1
                else:
                    charMap[s[right]] -= 1
            else:
                left = right + 1
                charMap = char.copy()
            
            if all(v == 0 for v in charMap.values()):
                res.append(left)
                charMap[s[left]] += 1
                left += 1
        
        return res
