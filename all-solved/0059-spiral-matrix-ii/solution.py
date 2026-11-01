class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]

        result = [[0 for i in range(n)] for i in range(n)]

        top, bottom = 0, n - 1
        left, right = 0, n - 1
        direction = "right"

        i = 1
        while top <= bottom and left <= right:
            if direction == "right":
                for j in range(left, right + 1):
                    result[top][j] = i
                    i += 1
                top += 1
                direction = "bottom"

            elif direction == "bottom":
                for j in range(top, bottom + 1):
                    result[j][right] = i
                    i += 1
                right -= 1
                direction = "left"

            elif direction == "left":
                for j in range(right, left - 1, -1):
                    result[bottom][j] = i
                    i += 1
                bottom -= 1
                direction = "top"

            elif direction == "top":
                for j in range(bottom, top - 1, -1):
                    result[j][left] = i
                    i += 1
                left += 1
                direction = "right"

        return result
