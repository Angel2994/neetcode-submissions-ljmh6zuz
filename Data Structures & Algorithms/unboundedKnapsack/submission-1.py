class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity
        prevRow = [0] * (n + 1)
        for c in range(n + 1):
            if weight[0] <= c:
                prevRow[c] = profit[0] + prevRow[c - weight[0]]

        for i in range(1, m):
            curRow = [0] * (n + 1)
            for j in range(n + 1):
                skip = prevRow[j]
                include = 0
                if j - weight[i] >= 0:
                    include = profit[i] + curRow[j - weight[i]]
                curRow[j] = max(skip, include)
            prevRow = curRow
        return prevRow[-1]