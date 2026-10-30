class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # h = len(haystack) # 3
        # n = len(needle) # 1

        # if (n > h): return -1
        # if h == 1: return 0

        # h_idx = n-1
        # while (h_idx < h) :
        #     n_idx = n-1
        #     temp = h_idx
        #     while (needle[n_idx] == haystack[h_idx]) :
        #         n_idx -= 1
        #         h_idx
            
        # return index of haystack.inclide(needle)

        return haystack.find(needle)
