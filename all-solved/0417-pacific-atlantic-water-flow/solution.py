class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        if rows == 1 and cols == 1:
            return [[0, 0]]

        pacific_q = deque()
        atlantic_q = deque()
        pacific_set = set()
        atlantic_set = set()

        for i in range(rows):
            pacific_q.append((i, 0))
            pacific_set.add((i, 0))
        for j in range(cols):
            pacific_q.append((0, j))
            pacific_set.add((0, j))

        for i in range(rows):
            atlantic_q.append((i, cols - 1))
            atlantic_set.add((i, cols - 1))
        for j in range(cols):
            atlantic_q.append((rows - 1, j))
            atlantic_set.add((rows - 1, j))

        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]

        while pacific_q:
            i, j = pacific_q.popleft()

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (0 <= r < rows and 
                    0 <= c < cols and 
                    (r, c) not in pacific_set and
                    heights[r][c] >= heights[i][j] 
                    ):
                    pacific_set.add((r, c))
                    pacific_q.append((r, c))
        
        while atlantic_q:
            i, j = atlantic_q.popleft()

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (0 <= r < rows and 
                    0 <= c < cols and 
                    (r, c) not in atlantic_set and
                    heights[r][c] >= heights[i][j] 
                    ):
                    atlantic_set.add((r, c))
                    atlantic_q.append((r, c))

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific_set and (i ,j) in atlantic_set:
                    res.append([i, j])
        
        return res
