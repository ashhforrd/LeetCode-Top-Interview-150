class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
                        
        distances = { node: float('inf') for node in range(1, n + 1) }
        distances[k] = 0

        heap = [(0, k)]

        while heap:
            currDistance, currNode = heapq.heappop(heap)

            if currDistance > distances[currNode]:
                continue
            
            for neighbor, weight in graph[currNode]:
                newDistance = currDistance + weight

                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance

                    heapq.heappush(heap, (newDistance, neighbor))
        
        if any(v == float('inf') for v in distances.values()):
            return -1
        return max(distances.values())
