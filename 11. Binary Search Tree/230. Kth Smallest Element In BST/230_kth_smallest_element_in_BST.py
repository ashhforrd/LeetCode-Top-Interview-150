# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        
        def getValue(root, nums):
            nums += [root.val]

            if root.left:
                getValue(root.left, nums)
            if root.right:
                getValue(root.right, nums)

        getValue(root, nums)
        nums.sort()

        return nums[k-1]