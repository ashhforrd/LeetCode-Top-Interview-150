class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        res = [[float('inf') for _ in range(cols)] for _ in range(rows)]

        q = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i, j, 0))
        
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]

        while q:
            i, j, distance = q.popleft()

            res[i][j] = min(res[i][j], distance)

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    q.append((r, c, distance + 1))
        
        return res
