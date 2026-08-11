class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        island = 0
        visited = set()

        def bfs(i, j):
            directions = [
                [-1, 0],
                [0, 1],
                [1, 0],
                [0, -1]
            ]

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    visited.add((i, j))
                    bfs(i, j)

        return island
