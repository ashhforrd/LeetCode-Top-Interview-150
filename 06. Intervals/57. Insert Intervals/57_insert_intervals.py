class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        result = []
        current = intervals[0]

        for j in range(1, len(intervals)):
            if current[1] >= intervals[j][0]:
                current = [current[0], max(current[1], intervals[j][1])]
            else:
                result.append(current)
                current = intervals[j]
        
        result.append(current)
        return result
