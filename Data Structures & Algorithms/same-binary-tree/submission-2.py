# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        q_p = deque([p])
        q_q = deque([q])

        while q_p and q_q:
            p_size = len(q_p)
            q_size = len(q_q)            
            for _ in range (p_size):
                p_top = q_p.popleft()
                q_top = q_q.popleft()

                if p_top is None and q_top is None:
                    continue
                if p_top is None or q_top is None or q_top.val != p_top.val:
                    return False
                
                q_p.append(p_top.left) 
                q_q.append(q_top.left)
                q_p.append(p_top.right) 
                q_q.append(q_top.right)

        return True

        