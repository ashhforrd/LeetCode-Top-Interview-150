"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodes = {}

        curr = head
        while curr:
            nodes[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = nodes[curr]

            if curr.next:
                copy.next = nodes[curr.next]
            else:
                copy.next = None
            
            if curr.random:
                copy.random = nodes[curr.random]
            else:
                copy.random = None
            
            curr = curr.next
        
        return nodes[head]