class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        fibb = [1,2]

        for i in range(2, n):
            steps = fibb[i-1] + fibb[i-2]
            fibb.append(steps)
        
        return fibb[-1]
