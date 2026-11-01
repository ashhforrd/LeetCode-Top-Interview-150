import math 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = m - 1
        col = n - 1

        total = row + col

        return int(math.factorial(total) / ( math.factorial(row) * math.factorial(total-row) ) )
