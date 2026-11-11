class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []
        count = [0] * n

        for start, end in meetings:

            while busy and busy[0][0] <= start:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))

            else:
                availableTime, room = heapq.heappop(busy)
                newEnd = availableTime + duration
                heapq.heappush(busy, (newEnd, room))

            count[room] += 1

        return max(
            range(n),
            key=lambda room: (count[room], -room)
        )
