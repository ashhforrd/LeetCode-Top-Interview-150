# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = [0]

        def dfs(root, val):
            if not root:
                return 

            if root.val >= val:
                good[0] += 1
            
            val = max(val, root.val)
            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, root.val)
        return good[0]
