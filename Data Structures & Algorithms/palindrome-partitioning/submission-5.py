class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        def backtracking(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPartition(s[i:j + 1]):
                    part.append(s[i: j + 1])
                    backtracking(j + 1)
                    part.pop()
            

        backtracking(0)
        return res
    
    def isPartition(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

