class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a, count_b = s.count('a'), 0

        res = count_a
        for c in s:
            if c == 'a':
                count_a -= 1
            elif c == 'b':
                count_b += 1

            res = min(res, count_a + count_b)
        
        return res
