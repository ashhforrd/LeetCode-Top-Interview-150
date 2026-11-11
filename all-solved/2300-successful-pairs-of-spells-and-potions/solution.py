class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        potions.sort()

        res = []

        for s in spells:
            left, right = 0, len(potions) - 1

            total = 0
            while left <= right:
                mid = (right + left) // 2

                temp = s * potions[mid]

                if temp >= success:
                    right = mid - 1
                    total = len(potions) - mid
                else:
                    left = mid + 1
            
            res.append(total)
        
        return res
