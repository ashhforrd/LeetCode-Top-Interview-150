class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mp = {}

        for w in words:
            mp[w] = mp.get(w, 0) + 1
        
        srtd = dict(sorted(mp.items(), key=lambda item: item[1]))

        heap = []
        for s in srtd:
            heapq.heappush(heap, (-srtd[s], s))

        res = []
        for i in range(k):
            _, word = heapq.heappop(heap)
            res.append(word)
        
        return res
