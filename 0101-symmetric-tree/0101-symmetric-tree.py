# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def isMirror(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            l1 = isMirror(p.right,q.left)
            l2 = isMirror(p.left,q.right)
            return l1 and l2
        
        return isMirror(root.left,root.right)
        