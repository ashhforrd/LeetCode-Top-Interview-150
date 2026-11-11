class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or not grid:
            return -1            

        n = len(grid) 

        if n == 1 and grid[0][0] == 0:
            return 1       

        q = deque([(0, 0, 1)])
        visited = set((0, 0))

        while q:
            i, j, path = q.popleft()

            directions = [
                [1, 0],
                [0, 1],
                [1, 1],
                [-1, 1],
                [-1, 0],
                [-1, -1],
                [0, -1],
                [1, -1]
            ]

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if r == n - 1 and c == n - 1 and grid[r][c] == 0:
                    return path + 1

                if (r, c) not in visited and 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c, path + 1))
                
        return -1
