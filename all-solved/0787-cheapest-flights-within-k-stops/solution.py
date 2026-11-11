class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for source, destination, cost in flights:
            graph[source].append((destination, cost))
        
        flightHeap = []
        heapq.heappush(flightHeap, (0, 0, src)) 

        cheapest = [[float("inf")] * (k + 2) for _ in range(n)]
        cheapest[src][0] = 0

        while flightHeap:
            cost, flight, source = heapq.heappop(flightHeap)
                   
            if source == dst:
                return cost

            for destination, cst in graph[source]:
                newCost = cost + cst
                newFlights = flight + 1

                if newFlights <= k + 1:
                    if newCost < cheapest[destination][newFlights]:
                        cheapest[destination][newFlights] = newCost
                        heapq.heappush(flightHeap, (newCost, newFlights, destination))
            
        return -1
