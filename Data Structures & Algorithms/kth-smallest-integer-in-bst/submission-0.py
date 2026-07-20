# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.val = k

        def dfs(root):
            if not root:
                return math.inf

            val1 = dfs(root.left)
            if val1 != math.inf:
                return val1

            self.val -= 1
            if self.val == 0:
                return root.val

            return dfs(root.right)

        return dfs(root)