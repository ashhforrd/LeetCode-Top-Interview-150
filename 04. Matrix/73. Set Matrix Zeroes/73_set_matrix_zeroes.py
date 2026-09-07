class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x_to_zero = set()
        y_to_zero = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x_to_zero.add(i)
                    y_to_zero.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in x_to_zero or j in y_to_zero:
                    matrix[i][j] = 0