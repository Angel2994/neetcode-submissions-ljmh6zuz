class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        rows = len(profit) - 1
        prevRow = [0] *  (capacity + 1)
        for c in range(capacity + 1):
            if weight[0] <= c:
                prevRow[c] = profit[0]
    
        for i in range(1, rows + 1):
            currRow = [0] * (capacity + 1)
            for j in range( capacity + 1):
                skip = prevRow[j]
                include = 0
                if j - weight[i] >= 0:
                    include = profit[i] + prevRow[j - weight[i]]
                currRow[j] = max(skip, include)
            prevRow = currRow
        return prevRow[-1]
