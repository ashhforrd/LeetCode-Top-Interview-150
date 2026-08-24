class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        max = 0

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            result.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in result:
                    result.add(s[j])
                else:
                    result = set()
                    break

                if len(result) > max:
                    max = len(result)

        return max if max != 0 else 1