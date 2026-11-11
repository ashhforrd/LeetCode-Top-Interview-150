class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)

        visited = set()
        queue = deque()

        directions = [
                [-1, 0],
                [1, 0],
                [0, -1],
                [0, 1]
            ]

        def bfs(i, j):
            q = deque([(i, j)])

            while q:
                i, j = q.popleft()

                for dr, dc in directions:
                    r, c = i + dr, j + dc
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        queue.append((r, c, 0))
                        visited.add((r, c))

        island = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    queue.append((i, j, 0))
                    bfs(i, j)

                    island = True
                    break
            if island:
                break
        
        while queue:
            i, j, bridge = queue.popleft()

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                    if grid[r][c] == 1:
                        return bridge
                    elif grid[r][c] == 0:
                        queue.append((r, c, bridge + 1))
                        visited.add((r, c))
