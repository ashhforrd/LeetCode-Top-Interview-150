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
        
        hashNode = {}

        current = head
        while current:
            hashNode[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            copyNode = hashNode[current]

            if current.next:
                copyNode.next = hashNode[current.next]
            else:
                copyNode.next = None
            
            if current.random:
                copyNode.random = hashNode[current.random]
            else:
                copyNode.random = None
        
            current = current.next
        
        return hashNode[head]