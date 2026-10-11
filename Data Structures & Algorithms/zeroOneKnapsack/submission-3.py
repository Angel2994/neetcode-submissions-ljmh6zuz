class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        m = capacity
        dp = [[0] * (m + 1) for row in range(n)]
        print(dp)
        for i in range(n):
            dp[i][0] = 0
        for c in range(m + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        
        for i in range(1, n):
            for j in range(1, m + 1):
                skip = dp[i - 1][j]
                include = 0
                if j - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][j - weight[i]]
                dp[i][j] = max(skip, include)
        return dp[n - 1][m]

        