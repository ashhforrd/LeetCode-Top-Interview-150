class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))

        res = ""
        for i in range(n):
            res = res + word1[i] + word2[i] 

        if len(word1) > len(word2):
            res = res + word1[i + 1:]
        else:
            res = res + word2[i + 1:]
        
        return res
