class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(max_profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return max_profit
        


tests = [
    (
        ([7, 1, 5, 3, 6, 4],),
        5,
    ),
    (
        ([7, 6, 4, 3, 1],),
        0,
    )
]