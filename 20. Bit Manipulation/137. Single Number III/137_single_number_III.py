class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for n in nums:
                bit = (n >> i) & 1
                if bit == 1:
                    count += 1
                
            result = result | (count % 3) << i
        
        if result & (1 << 31):
            result -= (1 << 32)

        return result