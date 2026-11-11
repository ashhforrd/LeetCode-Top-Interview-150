# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        res = [float('-inf')]

        def dfs(root, maxAnc, minAnc):
            if not root:
                return
            
            diff = max(abs(maxAnc - root.val), abs(minAnc - root.val))

            res[0] = max(res[0], diff)
            
            maxAnc = max(maxAnc, root.val)
            minAnc = min(minAnc, root.val)

            dfs(root.left, maxAnc, minAnc)
            dfs(root.right, maxAnc, minAnc)
            
        dfs(root, root.val, root.val)
        return res[0]
