class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = Counter(s)
        t_set = Counter(t)

        for c in t:
            if c not in s_set or s_set[c] < t_set[c]:
                return c
