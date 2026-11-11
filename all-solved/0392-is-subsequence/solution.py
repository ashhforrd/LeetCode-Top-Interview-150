class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # char_set = set(t)
        
        # for c in s:
        #     if c not in char_set:
        #         return False
        
        # return True

        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                j += 1
                i += 1
            else:
                i += 1
        
        if j == len(s):
            return True
        else:
            return False
