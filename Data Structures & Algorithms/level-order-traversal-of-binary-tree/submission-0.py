# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)

        while len(q) > 0:
            levelNodes = []
            for i in range(len(q)):
                elem = q.popleft()
                levelNodes.append(elem.val)
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
            ans.append(levelNodes)
        
        return ans
        