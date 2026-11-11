from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        start = (0, 0)
        litterIndex = {}
        litter = 0
        step = 0
        m, n = len(classroom), len(classroom[0])

        # Search Start Position and assign index to each litter
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)

                elif classroom[i][j] == "L":
                    litterIndex[(i, j)] = litter
                    litter += 1

        # mask = litter that has been cleaned
        mask = 0

        q = deque([
            (start[0], start[1], energy, mask, step)
        ])

        # (i, j, mask) -> maximum energy seen
        visited = {
            (start[0], start[1], mask): energy
        }

        directions = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]

        # All litter bits are 1
        allCleaned = (1 << litter) - 1

        while q:
            i, j, currentEnergy, mask, stepCount = q.popleft()

            if mask == allCleaned:
                return stepCount

            for d in directions:
                xi, yj = i + d[0], j + d[1]

                if (
                    xi >= 0 and xi < m
                    and yj >= 0 and yj < n
                    and currentEnergy > 0
                    and classroom[xi][yj] != "X"
                ):
                    updatedMask = mask
                    updatedCurrentEnergy = currentEnergy

                    # Clean litter
                    if classroom[xi][yj] == "L":
                        index = litterIndex[(xi, yj)]
                        updatedMask |= (1 << index)

                    # Move costs 1 energy
                    updatedCurrentEnergy -= 1

                    # Recharge after arriving at R
                    if classroom[xi][yj] == "R":
                        updatedCurrentEnergy = energy

                    state = (xi, yj, updatedMask)

                    # Only explore if we arrive with more energy
                    if (
                        state not in visited
                        or updatedCurrentEnergy > visited[state]
                    ):
                        visited[state] = updatedCurrentEnergy

                        q.append([
                            xi,
                            yj,
                            updatedCurrentEnergy,
                            updatedMask,
                            stepCount + 1
                        ])

        return -1
