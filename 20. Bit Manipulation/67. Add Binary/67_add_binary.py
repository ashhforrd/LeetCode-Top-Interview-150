class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        n = max(len(a), len(b))

        a = a.zfill(n)
        b = b.zfill(n)

        for i in range(n-1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            result = str(total % 2) + result
            carry = total // 2

        
        return str(carry) + result if carry else result