# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# the left child becomes the right child

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs (node):
            if node is None:
                return None
            
            temp_node = node.left
            node.left = node.right
            node.right = temp_node
        
            dfs(node.left)
            dfs(node.right)
            return node
        
        return dfs (root)