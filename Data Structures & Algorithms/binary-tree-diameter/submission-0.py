# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0 # global decalation; var needs to be available in every recurssive call
        def dim (root):
            if not root:
                return 0
            left = dim(root.left)
            right = dim(root.right)
            self.maxD = max(self.maxD, (left+right))
            return max(left, right)+1
        dim(root)
        return self.maxD
            
            