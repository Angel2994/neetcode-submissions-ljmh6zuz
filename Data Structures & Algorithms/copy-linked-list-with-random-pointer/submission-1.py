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
        oldToCopy = {None: None}
        curr = head
        #first pass map original node to copy node
        #iterate through entire list and create nodes with correct val
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        #second pass set the next and random correctly
        #map allows you to look up where random points to in O(1) since could point anywhere u need mep 
        while curr:
            node = oldToCopy[curr]
            node.next = oldToCopy[curr.next]
            node.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]

            
            
