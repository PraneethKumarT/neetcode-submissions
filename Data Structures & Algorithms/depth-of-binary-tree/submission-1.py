# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        level = 0
        q = deque()
        q.append(root)

        while len(q) > 0:
            for i in range(len(q)):
                elem = q.popleft()
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            level += 1
        
        return level

        