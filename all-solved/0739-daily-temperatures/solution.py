class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                _, index = stack.pop()
                res[index] = i - index
            
            stack.append([temperature, i])
        
        return res
