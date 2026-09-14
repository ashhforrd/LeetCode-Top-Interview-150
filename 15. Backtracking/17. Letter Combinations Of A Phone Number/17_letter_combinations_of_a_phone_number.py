class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = [""]

        for d in digits:
            chars = []
            for n in result:
                for c in mapping[d]:
                    chars.append(n + c)
            result = chars
        
        return result