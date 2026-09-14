class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "_" + word1
        word2 = "_" + word2

        n, m = len(word1), len(word2)

        dp_array = [[0 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp_array[i][j] = j
                    continue
                elif j == 0:
                    dp_array[i][j] = i
                    continue
                
                top = dp_array[i-1][j] if i != 0 else 0
                left = dp_array[i][j-1] if j != 0 else 0
                top_left = dp_array[i-1][j-1] if (i != 0 and j != 0) else 0
                 
                if word1[i] == word2[j]:
                    dp_array[i][j] = dp_array[i-1][j-1]
                else:
                    dp_array[i][j] = min(top, left, top_left) + 1
        
        return dp_array[-1][-1]