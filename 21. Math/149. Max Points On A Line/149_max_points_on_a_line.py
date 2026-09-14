from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n
        
        maximum = 1

        for i in range(len(points)):
            slopeCount = {}

            xi, yi = points[i]

            for j in range(i + 1, len(points)):
                xj, yj = points[j]

                dx, dy = xj - xi, yj - yi
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                if dx < 0:
                    dx *= -1
                    dy *= -1

                if dx == 0:
                    dy = 1

                if dy == 0:
                    dx = 1
                
                slope = (dx, dy)

                slopeCount[slope] = slopeCount.get(slope, 1) + 1

                maximum = max(maximum, slopeCount[slope])
        
        return maximum