# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        res = []

        def dfs(root, path):

            path = path + f"->{str(root.val)}"

            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

            if not root.left and not root.right:
                res.append(path)
        
        if root.left:
            dfs(root.left, f"{str(root.val)}")
        
        if root.right:
            dfs(root.right, f"{str(root.val)}")
        
        if not root.left and not root.right:
            res.append(f"{str(root.val)}")

        return res
