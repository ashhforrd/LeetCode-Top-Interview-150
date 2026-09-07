class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.generate(result, [], 1, n, k)
        return result

    def generate(self, result, temp, start, n, k):
        if len(temp) == k:
            result.append(temp)
            return
        
        for i in range(start, n+1):
            self.generate(result, temp + [i], i + 1, n, k)