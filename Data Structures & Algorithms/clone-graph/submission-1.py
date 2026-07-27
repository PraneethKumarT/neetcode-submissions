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

        q = deque([node])

        while q:
            elem = q.popleft()

            for neighbor in elem.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clone[elem].neighbors.append(clone[neighbor])
            
            

        return root


        