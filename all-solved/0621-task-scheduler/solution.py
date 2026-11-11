class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        sequence = 0
        longest = 0

        taskCount = {} 
        for task in tasks:
            taskCount[task] = taskCount.get(task, 0) + 1
            longest = max(longest, taskCount[task])
            
        heap = []
        for task in taskCount:
            interval = 0
            for i in range(taskCount[task]):
                heapq.heappush(heap, ([interval, task]))
                interval += n + 1

        # Solusi 1
        counter = 0
        while heap:
            order = heap[0][0]

            if order <= counter:
                _, task = heapq.heappop(heap)
                        
            counter += 1
            sequence += 1
        
        return sequence

        # Solusi 2
        # idleCount = (n + 1) - len(taskCount)
        # idleCount *= (longest - 1)

        # while heap:
        #     _, task = heapq.heappop(heap)
        #     sequence += 1
        
        # print("SEQUENCE", sequence)
        # print("IDLE COIUNT", idleCount)

        # return sequence + idleCount if idleCount > 0 else sequence
