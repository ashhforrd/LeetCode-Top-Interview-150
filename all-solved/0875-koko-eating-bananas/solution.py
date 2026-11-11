import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        left = 1
        right = max(piles)

        k = right

        def getHours(speed):
            hour = 0

            for p in piles:
                hour += math.ceil(p / speed)
            
            return hour

        while left <= right:
            speed = (left + right) // 2

            hours = getHours(speed)

            if hours <= h:
                k = speed
                right = speed - 1
            else:
                left = speed + 1
        
        return k
