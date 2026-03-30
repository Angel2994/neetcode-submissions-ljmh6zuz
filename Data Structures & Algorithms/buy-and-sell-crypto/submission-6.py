class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 1
        price = 0
        while right < len(prices):
            if prices[right] - prices[left] > 0:
                currPrice = prices[right] - prices[left]
                price = max(price, currPrice)
                right += 1
            else:
                left = right
                right += 1
        return price
