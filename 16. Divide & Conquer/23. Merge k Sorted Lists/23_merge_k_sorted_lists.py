"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            same = True

            for i in range(size):
                for j in range(size):
                    if grid[r][c] != grid[r + i][c + j]:
                        same = False
                        break
                if not same:
                    break
            
            if same:
                return Node(grid[r][c], True)
            
            size = size // 2
            topLeft = dfs(r, c, size)
            topRight = dfs(r, c + size, size)
            bottomLeft = dfs(r + size, c, size)
            bottomRight = dfs(r + size, c + size, size)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0, 0, len(grid))