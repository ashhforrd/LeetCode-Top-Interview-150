class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # res = []

        # heap = []
        # for i in range(len(arr)):
        #     heapq.heappush(heap, (abs(arr[i] - x), i, arr[i]))
        
        # for _ in range(k):
        #     _, _, n = heapq.heappop(heap)
        #     res.append(n)
        
        # return res

        l, r = 0, len(arr) - k

        while l < r:
            mid = (l + r) // 2

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        
        return arr[l: l + k]
