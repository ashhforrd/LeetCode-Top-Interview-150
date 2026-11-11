class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        clips.sort()

        total = 0
        covered = 0

        i = 0
        while covered < time:
            endMax = float('-inf')
            while i < len(clips) and clips[i][0] <= covered:
                start, end = clips[i]
                endMax = max(endMax, end)
                i += 1
            
            if endMax == float('-inf'):
                return -1

            covered = max(covered, endMax) 
            total += 1
        
        return total
