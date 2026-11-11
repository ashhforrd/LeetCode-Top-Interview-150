class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        res = [0] * len(boxes)

        balls, moves = 0, 0

        for i in range(len(boxes)):
            moves += balls
            res[i] += moves
            balls += int(boxes[i])

        balls, moves = 0, 0

        for i in reversed(range(len(boxes))):
            moves += balls
            res[i] += moves
            balls += int(boxes[i])

        return res
