# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []

        def dfs(node, maxVal):
            if not node:
                return None
            
            if node.val >= maxVal:
                ans.append(node.val)

            maxVal = max(maxVal, node.val)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        dfs(root, root.val)
        
        return len(ans)

"""


    3
   3. N
  4. 2 
"""