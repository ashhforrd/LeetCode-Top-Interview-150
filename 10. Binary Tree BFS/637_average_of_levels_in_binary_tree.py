# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        
        q = deque([root])
        output = []

        while q:
            qLen = len(q)
            avg = 0
            nums = 0

            for i in range(qLen):
                node = q.popleft()

                if node:
                    avg += node.val
                    nums += 1
                    q.append(node.left)
                    q.append(node.right)
            
            if nums > 0:
                output.append(avg/nums)
            
        return output