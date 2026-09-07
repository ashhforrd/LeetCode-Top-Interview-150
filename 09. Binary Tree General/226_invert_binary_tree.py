# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        result = TreeNode(root.val)

        self.generateLeaf(root, result)

        return result
    
    def generateLeaf(self, root, result):
        if not root:
            return
            
        if root.right:
            result.left = TreeNode(root.right.val)
            self.generateLeaf(root.right, result.left)


        if root.left:
            result.right = TreeNode(root.left.val)
            self.generateLeaf(root.left, result.right)
        
