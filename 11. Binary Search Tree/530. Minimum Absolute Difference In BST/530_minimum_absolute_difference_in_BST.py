# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = []
        self.getValue(root, nums)
        nums.sort()

        minValue = float('inf')

        for i in range(1, len(nums)):
            minValue = min(minValue, nums[i] - nums[i - 1])

        return minValue

    def getValue(self, node, nums):
        nums += [node.val]

        if node.left:
            self.getValue(node.left, nums)
        if node.right:
            self.getValue(node.right, nums)