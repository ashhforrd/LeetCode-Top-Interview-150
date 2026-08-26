class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0

        for _ in range(32):
            bit = n & 1
            if bit == 1:
                counter += 1
            n = n >> 1
        
        return counter