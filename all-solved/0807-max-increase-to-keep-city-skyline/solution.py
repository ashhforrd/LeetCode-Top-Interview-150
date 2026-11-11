class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        n = len(grid)
        rowsMax, colsMax = [0] * n, [0] * n

        for i in range(n):
            rowsMax[i] = max(grid[i])
            for j in range(n):
                colsMax[j] = max(colsMax[j], grid[i][j])

        total = 0
        for i in range(n):
            for j in range(n):
                total += (min(rowsMax[i], colsMax[j]) - grid[i][j])
        
        return total
