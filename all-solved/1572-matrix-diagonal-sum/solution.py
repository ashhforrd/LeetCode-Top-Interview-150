class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total = 0

        visited = set()

        for i in range(len(mat)):
            total += mat[i][i]
            visited.add((i, i))
                        
        for j in range(len(mat)):
            if (j, len(mat) - j - 1) not in visited:
                total += mat[j][len(mat) - j - 1]
            
                print(total)
    
        return total
