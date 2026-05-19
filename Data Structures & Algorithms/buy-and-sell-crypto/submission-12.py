class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l,r = 0, 1
        while r < len(prices):
            if prices[r] - prices[l] > 0:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            else:
                l = r 
            r += 1
        return maxProfit