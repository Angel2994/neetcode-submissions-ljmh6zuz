class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        m = capacity
        
        prevRow = [0] * (m + 1)
        for c in range(m + 1):
            if weight[0] <= c:
                prevRow[c] = profit[0]
        for i in range(1, n):
            currRow = [0] * (m + 1)
            for j in range(1, m + 1):
                skip = prevRow[j]
                include = 0
                if j - weight[i] >= 0:
                    include = profit[i] + prevRow[j - weight[i]]
                currRow[j] = max(skip, include)
            prevRow = currRow
        return prevRow[-1]

        