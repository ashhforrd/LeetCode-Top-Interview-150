class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = []
        for i in range(numRows):
            result.append([])

        currentRow = 0
        direction = "Down"
   
        for i in range(len(s)):
            result[currentRow].append(s[i])

            if direction == "Down":
                currentRow += 1
            elif direction == "Up":
                currentRow -= 1

            if currentRow == numRows-1:
                direction = "Up"
            elif currentRow == 0:
                direction = "Down"
            
        return "".join("".join(row) for row in result)
