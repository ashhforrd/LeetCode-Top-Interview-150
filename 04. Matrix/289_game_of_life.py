class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        newBoard = [row[:] for row in board]

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
                liveNeighbors = 0
                deadNeighbors = 0

                for row, col in directions:
                    if i + row >= 0 and j + col >= 0 and i + row < len(board) and j + col < len(board[0]):
                        if board[i+row][j+col] == 1:
                            liveNeighbors += 1
                        else:
                            deadNeighbors += 1
                    
                if board[i][j] == 1:
                    if liveNeighbors < 2:
                        newBoard[i][j] = 0
                    if liveNeighbors == 2 or liveNeighbors == 3:
                        continue
                    if liveNeighbors > 3:
                        newBoard[i][j] = 0

                if board[i][j] == 0 and liveNeighbors == 3:
                    newBoard[i][j] = 1
        
        board[:] = newBoard

                    