# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        result = TreeNode(root.val, None, None)

        q = deque([root])
        rows = []

        i = 0
        while q:
            qLen = len(q)
            row = []

            for j in range(qLen):
                node = q.popleft()
                row.append(node)

                if node.left:
                    q.append(node.left) 
                if node.right:   
                    q.append(node.right)

            if i % 2 == 1:
                row.reverse()
            rows.append(row)
            i += 1
                
        i = 1
        q = deque([result])

        while q and i < len(rows):
            qLen = len(q)

            row = deque(rows[i])

            for j in range(qLen):
                node = q.popleft()

                node.left = row.popleft()
                node.right = row.popleft()

                q.append(node.left)
                q.append(node.right)

            i += 1

        return result
