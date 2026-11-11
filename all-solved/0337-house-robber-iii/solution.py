# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
    
        def dfs(root):
            if not root:
                return [0, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            take = root.val + left[1] + right[1]
            skip = max(left) + max(right)

            return [take, skip]

        return max(dfs(root))
