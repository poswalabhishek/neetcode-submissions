# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if subroot is a subset of root
        if subRoot is None:
            return True
        if root is None:
            return False

        def dfs (root, subroot):
            if root is None and subroot is None:
                return True
            
            if root is None or subroot is None or root.val != subroot.val:
                return False
            
            return dfs (root.left, subroot.left) and dfs (root.right, subroot.right)

        return dfs(root, subRoot) or self.isSubtree (root.left, subRoot) or self.isSubtree (root.right, subRoot)