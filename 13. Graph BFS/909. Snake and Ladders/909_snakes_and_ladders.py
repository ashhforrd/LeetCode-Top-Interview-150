from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(position):
            r = (position - 1) // length
            c = (position - 1) % length
            if r % 2:
                c = length - 1 - c
        
            return [r, c]
        
        q = deque()
        q.append([1,0]) # possition, moves
        visit = set()

        while q:
            position, moves = q.popleft()

            for i in range(1, 7):
                nextPosition = position + i
                r, c = intToPos(nextPosition)

                if board[r][c] != -1:
                    nextPosition = board[r][c]
                if nextPosition == length * length:
                    return moves + 1
                if nextPosition not in visit:
                    q.append([nextPosition, moves + 1])
                    visit.add(nextPosition)
        
        return -1