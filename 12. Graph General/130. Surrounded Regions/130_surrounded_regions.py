from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        visited = set()

        def bfs(i, j):
            q = deque([(i, j)])
            convert = [(i, j)]
            visited.add((i, j))

            directions = [
                [-1, 0],
                [0, 1],
                [1, 0],
                [0, -1]
            ]

            while q:
                i, j = q.popleft()

                for dr, dc in directions:
                    r, c = i + dr, j + dc

                    if r in range(len(board)) and c in range(len(board[0])) and (r, c) not in visited and board[r][c] == "O":
                        convert.append((r, c))
                        q.append((r, c))
                        visited.add((r, c))
            
            canConvert = True
            for r, c in convert:
                if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1:
                    canConvert = False
            
            if canConvert:
                for r, c in convert:
                    board[r][c] = "X"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    bfs(i, j)
