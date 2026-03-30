# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = k 
        res = 0
        def dfs(root):
            nonlocal kth, res
            if not root:
                return 
            dfs(root.left)
            kth -= 1
            if kth == 0:
                res = root.val
                return
            dfs(root.right)
        dfs(root)
        return res