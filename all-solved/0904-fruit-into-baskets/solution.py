class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        basket = defaultdict(int)
        maxFruit = 0

        l = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
    
                l += 1
         
            maxFruit = max(maxFruit, r - l + 1)
        
        return maxFruit
