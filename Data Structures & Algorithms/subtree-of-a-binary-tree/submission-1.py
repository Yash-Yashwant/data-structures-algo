# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def subSame(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            return p.val == q.val  and subSame(p.left, q.left) and subSame(p.right, q.right)


        def same(root, subRoot):
            if not root:
                return False
            if subSame(root, subRoot):
                return True

            return same(root.left, subRoot) or same(root.right, subRoot)

        return same(root, subRoot)
