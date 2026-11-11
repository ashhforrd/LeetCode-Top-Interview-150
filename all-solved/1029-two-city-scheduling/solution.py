class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        diff = []
        for i, cost in enumerate(costs):
            a, b = cost
            diff.append([b - a, i])
        
        total = 0
        diff.sort()

        for i, d in enumerate(diff):
            _, idx = d

            if i < len(costs) // 2:
                total += costs[idx][1]
            else:
                total += costs[idx][0]
        
        return total
