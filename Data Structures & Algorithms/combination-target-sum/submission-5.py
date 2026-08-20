class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        def backtracking(i, curSum):
            if curSum == target:
                res.append(combo.copy())
                return

            if i >= len(nums) or curSum > target:
                return 

            combo.append(nums[i])
            backtracking(i, curSum + nums[i])

            combo.pop()
            backtracking(i + 1, curSum)

        backtracking(0, 0)
        return res