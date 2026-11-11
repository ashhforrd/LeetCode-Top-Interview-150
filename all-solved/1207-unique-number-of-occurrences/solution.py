class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurences = {}

        for n in arr:
            occurences[n] = occurences.get(n, 0) + 1
        
        values = set()
        for v in occurences.values():
            if v in values:
                return False
            values.add(v)

        return True
