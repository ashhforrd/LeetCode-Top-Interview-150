class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        res = []

        rank = arr.copy()
        rank.sort()

        rankMap = {}
        count = 1
        for n in rank:
            if n not in rankMap:
                rankMap[n] = count
                count += 1
        
        for n in arr:
            res.append(rankMap[n])
        
        return res
