class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap = {}

        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in patternMap:
                if words[i] not in patternMap.values():
                    patternMap[pattern[i]] = words[i]
                else:
                    return False
            else:
                if words[i] != patternMap[pattern[i]]:
                    return False

        return True 