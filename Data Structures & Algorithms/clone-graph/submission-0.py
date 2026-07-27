"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clone = {}

        if not node:
            return
    
        root = Node(node.val, None)
        clone[node] = root

        q = deque()
        q.append(node)
        vis = []

        while len(q) > 0:
            for i in range(len(q)):
                elem = q.popleft()

                if elem in vis:
                    continue

                vis.append(elem)

                if elem not in clone:
                    clone[elem] = Node(elem.val, None)
                
                neighbors_copy = []
                for neighbor in elem.neighbors:
                    if neighbor not in clone:
                        clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                    neighbors_copy.append(clone[neighbor])
                
                clone[elem].neighbors = neighbors_copy

        return root


        