class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, partition = [], []
        def backtracking(i):
            if i == len(s):
                res.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.isPartition(s, i, j):
                    partition.append(s[i:j + 1])
                    backtracking(j + 1)
                    partition.pop()

        backtracking(0)
        return res
    
    def isPartition(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True