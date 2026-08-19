from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        hashPoints = {}
        for p in points:
            hashPoints[tuple((p[0], p[1]))] = {}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
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

                if tuple((dx, dy)) not in hashPoints[tuple((xi, yi))]:
                    hashPoints[tuple((xi, yi))][tuple((dx, dy))] = 2
                else:
                    hashPoints[tuple((xi, yi))][tuple((dx, dy))] += 1
        
        # Mencari value terbesar set dalam set
        maximum = 1

        for inner in hashPoints.values():
            if inner:
                maximum = max(maximum, max(inner.values()))

        return maximum