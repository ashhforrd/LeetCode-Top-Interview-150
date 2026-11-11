class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        longest, freqMax = float('-inf'), 0

        left = 0
        for right in range(len(s)):
            char[s[right]] = char.get(s[right], 0) + 1
            freqMax = max(freqMax, char[s[right]])

            if (right - left + 1) - freqMax > k:
                char[s[left]] -= 1
                left += 1
            
            longest = max(longest, (right - left + 1))
        
        return longest
