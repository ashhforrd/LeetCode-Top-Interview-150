class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1 

        status = "top"
        result = []

        while top <= bottom and left <= right:
            if status == "top":
                for i in range(left, right+1):
                    result.append(matrix[top][i])
                top += 1
                status = "right"
            elif status == "bottom":
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                status = "left"
            elif status == "right":
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
                status = "bottom"
            elif status == "left":
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
                status = "top"
        
        return result