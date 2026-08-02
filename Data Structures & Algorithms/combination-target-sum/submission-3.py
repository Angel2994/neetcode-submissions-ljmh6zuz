class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        def backtracking(i, total):
            if total == target:
                res.append(combo.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            backtracking(i, total + nums[i])

            combo.pop()
            backtracking(i + 1, total), 

        backtracking(0, 0)
        return res