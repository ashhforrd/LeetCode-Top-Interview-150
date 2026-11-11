class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        chars = {}
        for c in text:
            if c in 'balon':
                chars[c] = chars.get(c, 0) + 1
        
        need = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1,
        }

        total = float('inf')
        for c in need:
            if c not in chars:
                return 0
            
            total = min(total, chars[c] // need[c])
        
        return total
