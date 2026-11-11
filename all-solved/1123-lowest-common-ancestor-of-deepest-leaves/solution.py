# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        q = deque([root])

        lowest = []

        while q:
            qLen = len(q)
            lowest = []

            for _ in range(qLen):
                node = q.popleft()
                lowest.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        if len(lowest) == 1:
            return lowest[0]

        def dfs(root):
            if not root:
                return None
            
            if root == lowest[0] or root == lowest[-1]:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            return left or right
        
        return dfs(root)
