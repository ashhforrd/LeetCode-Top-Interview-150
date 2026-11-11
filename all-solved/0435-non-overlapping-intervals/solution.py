class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        overlap = 0
        currentEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if currentEnd > start:
                overlap += 1
                currentEnd = min(currentEnd, end)
            else:
                currentEnd = end
        
        return overlap
