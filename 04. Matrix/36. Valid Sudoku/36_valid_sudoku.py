class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_result = self.isRowValid(board, i)
            if row_result == False: return False
            for j in range(9):
                col_result = self.isColumnValid(board, j)
                if col_result == False: return False

                if i % 3 == 0 and j % 3 == 0:
                    box_result = self.isBoxValid(board, i, j)
                    if box_result == False: return False

        return True
 
    def isRowValid(self, board, row_idx) -> bool:
        nums = set()
        for i in range(9):
            num = board[row_idx][i]
            if num.isdigit():
                if num in nums:
                    return False
                else:
                    nums.add(num) 
        
        return True

    def isColumnValid(self, board, col_idx) -> bool:
        nums = set()
        for i in range(9):
            num = board[i][col_idx]
            if num.isdigit():
                if num in nums:
                    return False
                else:
                    nums.add(num) 
        
        return True

    def isBoxValid(self, board, row_idx, col_idx) -> bool:
        nums = set()
        for i in range(row_idx, row_idx+3):
            for j in range(col_idx, col_idx+3):
                num = board[i][j]
                if num.isdigit():
                    if num in nums:
                        return False
                    else:
                        nums.add(num)
        
        return True