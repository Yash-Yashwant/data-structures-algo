# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if not root:
                return 0 # if there is no root node then return 0 as depth
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right)+1

        return depth(root)    