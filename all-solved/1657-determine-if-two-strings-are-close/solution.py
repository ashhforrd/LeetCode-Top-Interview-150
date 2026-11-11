from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1 = Counter(word1)
        s2 = Counter(word2)

        return s1.keys() == s2.keys() and sorted(s1.values()) == sorted(s2.values())
