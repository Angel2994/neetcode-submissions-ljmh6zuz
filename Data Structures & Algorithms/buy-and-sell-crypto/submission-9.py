class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 1
        profit = 0
        
        while right < len(prices):
            if prices[right] - prices[left] > 0:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
        return profit 


        