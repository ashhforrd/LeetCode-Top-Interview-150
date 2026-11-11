# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        res = 0
        q = deque([[root, 1, 0]])
        prevLevel, prevNum = 0, 1

        while q:
            node, num, level = q.popleft()

            if level > prevLevel:
                prevNum = num
                prevLevel = level
            
            res = max(res, num - prevNum + 1)

            if node.left:
                q.append([node.left, num * 2, level + 1])
            if node.right:
                q.append([node.right, num * 2 + 1, level + 1])
        
        return res
