class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        longest = 0
        left = 0

        if len(s) == 0:
            return 0
        
        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[left])
                left += 1

            char.add(s[right])
            longest = max(longest, right - left + 1)

        return max(1, longest)