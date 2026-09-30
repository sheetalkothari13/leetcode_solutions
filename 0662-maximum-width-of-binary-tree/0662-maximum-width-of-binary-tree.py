# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue = deque([(root,0)])
        max_width = 0
        while queue:
            level_size = len(queue)
            first_position = queue[0][1]
            last_position = 0
            for _ in range(level_size):
                node,position = queue.popleft()
                last_position = position
                if node.left:
                    queue.append((node.left,2*position + 1))
                if node.right:
                    queue.append((node.right,2*position + 2))
            width = last_position - first_position + 1
            max_width = max(max_width,width)
        return max_width
        