# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        queue = deque([target])
        visited = {target}
        distance = 0
        while queue and distance < k:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])
            distance += 1
        return [node.val for node in queue]
        