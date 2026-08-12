class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        current = 0

        while current < len(gas) :
            tank += gas[current] - cost[current]

            if tank < 0: # kalau habis maka
                current += 1
                start = current
                tank = 0
            else:
                current += 1


        return start