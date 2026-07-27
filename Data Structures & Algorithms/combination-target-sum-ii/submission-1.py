class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combo = [], []
        candidates.sort()

        def backtracking(i, total):
            if (total == target):
                res.append(combo.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            backtracking(i + 1, total + candidates[i])

            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtracking(i + 1, total)

        backtracking(0, 0)
        return res


