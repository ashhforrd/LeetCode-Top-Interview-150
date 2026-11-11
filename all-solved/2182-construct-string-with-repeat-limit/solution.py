class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = Counter(s)
        heap = []

        for c in chars:
            heapq.heappush(heap, (-ord(c), c, chars[c]))
        
        answer, temp = "", ""
        while heap:
            _, char, amount = heapq.heappop(heap)
            
            limit = repeatLimit if not temp or char > temp[1] else 1
            while limit > 0 and amount > 0:
                answer += char
                limit -= 1
                amount -= 1

            if temp:
                heapq.heappush(heap, temp)
                temp = ""
            
            if amount > 0:
                temp = (-ord(char), char, amount)
        
        return answer
