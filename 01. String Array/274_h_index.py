class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        # [0, 1, 3, 5, 6]

        h_value = 0

        n = len(citations)

        if n == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        for i in range(n):
            if len(citations[i:]) >= min(citations[i], n - i):
                if min(citations[i], n - i) > h_value:
                    h_value = min(citations[i], n - i)
        
        return h_value