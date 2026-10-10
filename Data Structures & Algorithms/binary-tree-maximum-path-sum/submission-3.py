# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxValue = root.val
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal maxValue
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            currSum = root.val + left + right
            maxValue = max(currSum, maxValue)
            return root.val + max(left, right)
        dfs(root)
        return maxValue