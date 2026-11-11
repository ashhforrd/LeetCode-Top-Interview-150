class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if not trust:
            if n == 1:
                return 1
            else:
                return -1

        person = collections.defaultdict(list)
        trusting = set()

        for t in trust:
            person[t[0]].append(t[1])
            trusting.add(t[0])
        
        candidate = set()
        arr = []
        for i in range(1, n + 1):
            if i not in trusting:
                candidate.add(i)

            if all(i in v for v in person.values()):
                arr.append(i)
        
        if len(arr) != len(candidate):
            return -1
        if arr:
            return arr[0]

        return -1
