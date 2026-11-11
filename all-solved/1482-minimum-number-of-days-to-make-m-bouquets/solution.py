class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        left, right = min(bloomDay), max(bloomDay)

        def getBouquet(day):
            res, count = 0, 0

            for d in bloomDay:
                if d <= day:
                    count += 1
                else:
                    count = 0

                if count == k:
                    res += 1
                    count = 0
            
            return res

        minDay = float('inf')
        while left <= right:
            mid = (left + right) // 2

            bouquet = getBouquet(mid)

            if bouquet < m:
                left = mid + 1
            else:
                right = mid - 1
                minDay = min(minDay, mid)
        
        return minDay
