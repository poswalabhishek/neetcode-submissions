# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        level = 0

        while queue:
            for i in range (len(queue)):
                curr_top = queue.popleft()
                if curr_top.left:
                    queue.append(curr_top.left)
                if curr_top.right:
                    queue.append(curr_top.right)
            level += 1

        return level