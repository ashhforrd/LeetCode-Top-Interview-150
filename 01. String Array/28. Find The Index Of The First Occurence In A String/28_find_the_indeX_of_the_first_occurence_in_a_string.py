class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        if (n > h): return -1
        if h == 1: return 0

        for i in range(h-n+1): 
            count = 0
            for j in range(n):
            
                if haystack[i+j] == needle[j]:
                    count += 1
                
                if count == n:
                    return i

        return -1

    # return haystack.find(needle)
