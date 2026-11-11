class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # n = len(s1)
        # s = Counter(s1)

        # for i in range(len(s2) - n + 1):
        #     if s2[i] in s:
        #         mp = s.copy()
        #         for j in range(i, i + n):
        #             if s2[j] not in mp:
        #                 break
        #             mp[s2[j]] -= 1
                                
        #         if all(v == 0 for v in mp.values()):
        #             return True

        # return False

        # s, c = Counter(s1), Counter(s1)

        # l = 0
        # for r in range(len(s2)):
        #     if s2[r] in s:
        #         s[s2[r]] -= 1
            
        #     while any(v < 0 for v in s.values()) or (s2[r] not in s and s != c):
        #         if s2[l] in s:
        #             s[s2[l]] += 1
        #         l += 1
            
        #     if all(v == 0 for v in s.values()):
        #         return True
        
        # return False

        n = len(s1)

        if n > len(s2):
            return False
        
        target = Counter(s1)
        window = Counter(s2[:n])

        if window == target:
            return True

        for i in range(n, len(s2)):
            window[s2[i]] += 1
            window[s2[i - n]] -= 1

            if window == target:
                return True
        
        return False
