class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boards = [row[:] for row in board]

        directions = [
            [-1, -1],
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
            [0, 1],
            [-1, 1],
            [-1, 0]
        ]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live, dead = 0, 0

                for r, c in directions:
                    if (i + r >= 0 and j + c >= 0 and i + r < len(board) and j + c < len(board[0])):
                        if board[i + r][j + c] == 0:
                            dead += 1
                        else:
                            live += 1
                    
                if board[i][j] == 1:
                    if live < 2:
                        boards[i][j] = 0
                    elif live > 3:
                        boards[i][j] = 0
                
                elif board[i][j] == 0 and live == 3:
                    boards[i][j] = 1
        
        board[:] = boards