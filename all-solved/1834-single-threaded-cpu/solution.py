class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        
        tasks = [
            (enqueueTime, processingTime, index)
            for index, (enqueueTime, processingTime) in enumerate(tasks)
        ]
        tasks.sort(key=lambda x: x[0])

        processingHeap = []
                        
        currentTime, i = 0, 0

        while i < len(tasks) or processingHeap:

            if not processingHeap and currentTime < tasks[i][0]:
                currentTime = tasks[i][0]
            
            while i < len(tasks) and tasks[i][0] <= currentTime:
                enqueueTime, processingTime, index = tasks[i]
                heapq.heappush(processingHeap, (processingTime, index))
                i += 1
            
            processingTime, index = heapq.heappop(processingHeap)
            order.append(index)
            
            currentTime += processingTime    

        return order
