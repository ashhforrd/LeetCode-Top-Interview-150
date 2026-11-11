class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right: 
            cap = (left + right) // 2 

            def getDay(capacity):
                days, storage = 1, 0

                for w in weights:
                    if storage + w > capacity:
                        days += 1
                        storage = w
                    else:
                        storage += w
                
                return days

            day = getDay(cap)

            if day <= days:
                right = cap
            elif day > days:
                left = cap + 1

        return left
