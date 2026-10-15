class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []
        def backtracking(i):
            if i == len(nums):
                res.append(subsets.copy())
                return

            subsets.append(nums[i])
            backtracking(i + 1)

            subsets.pop()
            backtracking(i + 1)
        backtracking(0)
        return res