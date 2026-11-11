class Solution:
    def minOperations(self, s: str) -> int:
        operations = 0
        for i, c in enumerate(s):
            if (i % 2 == 0 and c == '1') or (i % 2 == 1 and c == '0'):
                operations += 1
        
        return min(operations, len(s) - operations)
