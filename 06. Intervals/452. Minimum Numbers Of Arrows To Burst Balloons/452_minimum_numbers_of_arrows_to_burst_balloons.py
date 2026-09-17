class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        arrow = 1
        currentEnd = points[0][1]

        for start, end in points[1:]:
            if start <= currentEnd:
                currentEnd = min(currentEnd, end)
            else:
                arrow += 1
                currentEnd = end
        
        return arrow