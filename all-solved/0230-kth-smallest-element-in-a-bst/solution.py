# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def getValue(root):
            heapq.heappush(heap, root.val)

            if root.left:
                getValue(root.left)
            if root.right:
                getValue(root.right)

        getValue(root)

        for _ in range(k - 1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
