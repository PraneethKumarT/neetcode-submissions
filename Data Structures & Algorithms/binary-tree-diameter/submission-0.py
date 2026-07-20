# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        l = self.diameterOfBinaryTree(root.left)
        r = self.diameterOfBinaryTree(root.right)

        depth = self.depth(root.left) + self.depth(root.right)

        return max(l , r, depth)
    
    def depth(self, root):
        if not root:
            return 0
        
        l = self.depth(root.left)
        r = self.depth(root.right)
        return max(l, r) + 1
        