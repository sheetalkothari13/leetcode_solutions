# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        columns = {}
        def dfs(node,row,col):
            if node is None:
                return
            if col not in columns:
                columns[col] = []
            columns[col].append((row,node.val))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        
        dfs(root,0,0)
        result = []
        for col in sorted(columns):
            columns[col].sort()

            level =[]
            for row,value in columns[col]:
                level.append(value)

            result.append(level)
        return result