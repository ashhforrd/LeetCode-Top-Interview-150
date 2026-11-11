# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            
            if p.val < root.val and q.val < root.val:
                left = dfs(root.left)
                right = None
            elif p.val > root.val and q.val > root.val:
                left = None
                right = dfs(root.right)
            else:
                return root
            return left or right
        
        return dfs(root)
