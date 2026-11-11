class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first = s[:len(s) // 2]
        second = s[len(s) // 2:]

        firstVocal, secondVocal = 0, 0

        vocals = 'aiueoAIUEO'

        for c in first:
            if c in vocals:
                firstVocal += 1
        for c in second:
            if c in vocals:
                secondVocal += 1
        
        return firstVocal == secondVocal
