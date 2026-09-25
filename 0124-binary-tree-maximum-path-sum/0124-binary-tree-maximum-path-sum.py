# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        global_max = float('-inf')
        def dfs(node):
            nonlocal global_max
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            through_node = max(0,left) + node.val + max(0,right)
            global_max = max(global_max,through_node)
            return node.val + max(0,left,right)
        
        dfs(root)
        return global_max
        