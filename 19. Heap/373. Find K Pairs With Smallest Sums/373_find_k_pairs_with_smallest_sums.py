class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs, res = [], []

        for i in range(len(nums1)):
            heapq.heappush(pairs, ((nums1[i] + nums2[0]), i, 0))
        
        while pairs and len(res) < k:
            _, i, j = heapq.heappop(pairs)

            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(pairs, ((nums1[i] + nums2[j + 1]), i, j + 1))
        
        return res