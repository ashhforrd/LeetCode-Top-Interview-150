class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (i > 0 and flowerbed[i - 1] == 1) or (i < len(flowerbed) - 1 and flowerbed[i + 1] == 1) or flowerbed[i] == 1:
                continue

            if n > 0:  
                flowerbed[i] = 1
                n -= 1
        
        return n == 0
