class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_on  = prices[0]
        for i in range(len(prices)):
            cost  = prices[i] - buy_on
            profit = max(cost,profit)

            buy_on = min(prices[i],buy_on)
        return profit


        
        