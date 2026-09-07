class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(r, c):
            ir, ic = r, c

            visited.add((i, j))
            q = deque()
            q.append((r, c))
            convert = []
            convert.append((r, c))
            canConvert = True

            while q:
                row, col = q.popleft()
                directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and (r, c) not in visited and board[r][c] == "O"):
                        visited.add((r, c))
                        q.append((r, c))
                        convert.append((r, c))
            
            for r, c in convert:
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    canConvert = False
            
            if canConvert:
                for r, c in convert:
                    board[r][c] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    bfs(i, j)