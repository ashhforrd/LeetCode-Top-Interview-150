class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])

        res = ""
        for i in range(l): # loop char dari str terpendek
            curr = strs[0][i]
            for j in range(1, len(strs)): # loop sisa char pada strs
                if i >= len(strs[j]) or strs[j][i] != curr:
                    return res
            
            res += curr
        
        return res
                