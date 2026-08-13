class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_index = 0

        for i in range(len(matrix)):
            if target <= matrix[i][0]:
                if matrix[i][0] == target: return True
                start_index = i-1 if i != 0 else 0
                break
            else:
                start_index = i

            

        return target in matrix[start_index]