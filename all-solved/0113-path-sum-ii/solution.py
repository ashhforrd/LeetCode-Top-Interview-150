# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        q = deque([(root, root.val, [root.val])])

        while q:
            node, currSum, path = q.popleft()

            if not node.left and not node.right and currSum == targetSum:
                result.append(path)
            if node.left:
                leftPath = path.copy()
                leftPath.append(node.left.val)
                q.append([node.left, currSum + node.left.val, leftPath])
            if node.right:
                rightPath = path.copy()
                rightPath.append(node.right.val)
                q.append([node.right, currSum + node.right.val, rightPath])

        return result
