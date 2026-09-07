class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        firstChar = word[0]
        m, n = len(board), len(board[0])

        def dfs(i, j, currChar, currWord, visited):
            visited.add((i, j))

            if currWord == word:
                return True

            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

            for dr, dc in directions:
                r, c = i + dr, j + dc

                if (r in range(m) and 
                    c in range(n) and 
                    (r, c) not in visited
                    ):
                    if (
                        currChar + 1 < len(word)
                        and board[r][c] == word[currChar + 1]
                    ):
                        if dfs(r, c, currChar + 1, currWord + word[currChar + 1], visited):
                            return True
            
            visited.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == firstChar:
                    visited = set()

                    if dfs(i, j, 0, firstChar, visited) == True:
                        return True
        
        return False