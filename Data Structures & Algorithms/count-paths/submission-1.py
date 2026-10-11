class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n
        for i in range(m - 2, -1, -1):
            currRow = [0] * n
            for j in range(n - 1, -1, -1):
                rightCol = currRow[j + 1] if (j + 1) < n else 0
                bottom = prevRow[j]
                currRow[j] = rightCol + bottom
            prevRow = currRow
        return prevRow[0]