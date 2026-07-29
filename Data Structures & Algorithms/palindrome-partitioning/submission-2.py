class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, combo = [], []
        def backtracking(i):
            if i == len(s):
                res.append(combo.copy())
                return res

            for j in range(i, len(s)):
                if self.isPartition(s, i, j):
                    combo.append(s[i: j + 1])
                    backtracking(j + 1)
                    combo.pop()

        backtracking(0)
        return res
    
    def isPartition(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
