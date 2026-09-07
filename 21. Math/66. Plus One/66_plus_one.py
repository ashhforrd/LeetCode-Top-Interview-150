class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(str(d) for d in digits))
        number += 1

        return [int(x) for x in str(number)]