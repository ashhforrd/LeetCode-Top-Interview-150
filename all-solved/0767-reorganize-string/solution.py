class Solution:
    def reorganizeString(self, s: str) -> str:  
        result = "" 

        char = {}
        for c in s: 
            char[c] = char.get(c, 0) + 1 
        
        maxHeap = [] 
        for key in char:  
            heapq.heappush(maxHeap, (-char[key], key)) 
        
        prev = None
        while maxHeap: 
            count, c = heapq.heappop(maxHeap) 
            result += c 

            print(result)

            if prev and prev[0] < 0:
                heapq.heappush(maxHeap, (prev[0], prev[1]))

            if count < 0:
                prev = [count + 1, c]
        
        if len(result) != len(s):
            return ""
        return result
