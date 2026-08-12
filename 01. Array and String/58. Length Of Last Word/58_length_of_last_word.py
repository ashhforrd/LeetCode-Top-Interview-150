class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.split()
        text = s.split()

        return len(text[-1])