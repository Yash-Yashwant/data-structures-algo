# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ls = []
        def inorder(root):
            if not root:
                return None
            
            inorder(root.left)
            self.ls.append(root.val)
            inorder(root.right)

        inorder(root)
        return self.ls