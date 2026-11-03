class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r not in range(rows) or 
                c not in range(cols) or 
                board[r][c] != word[i] or 
                (r, c) in visited):
                return False
            
            visited.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

        # firstChar = word[0]
        # m, n = len(board), len(board[0])

        # def dfs(i, j, currChar, currWord, visited):
        #     visited.add((i, j))

        #     if currWord == word:
        #         return True

        #     directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        #     for dr, dc in directions:
        #         r, c = i + dr, j + dc

        #         if (r in range(m) and 
        #             c in range(n) and 
        #             (r, c) not in visited
        #             ):
        #             if (
        #                 currChar + 1 < len(word)
        #                 and board[r][c] == word[currChar + 1]
        #             ):
        #                 if dfs(r, c, currChar + 1, currWord + word[currChar + 1], visited):
        #                     return True
            
        #     visited.remove((i, j))
        #     return False

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == firstChar:
        #             visited = set()

        #             if dfs(i, j, 0, firstChar, visited) == True:
        #                 return True
        
        # return False
