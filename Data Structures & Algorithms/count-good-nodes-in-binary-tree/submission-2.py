# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxValue):
            if not root:
                return 
            
            nonlocal res
            if root.val >= maxValue:
                res += 1
            maxValue = max(maxValue, root.val)
            dfs(root.left, maxValue)
            dfs(root.right, maxValue)
        dfs(root, root.val)
        return res