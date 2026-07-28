class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, partition = [], []
        def backtracking(i):
            if i >= len(s):
                res.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.isPartition(s, i, j):
                    partition.append(s[i:j + 1])
                    backtracking(j + 1)
                    partition.pop()

        backtracking(0)
        return res

    def isPartition(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True