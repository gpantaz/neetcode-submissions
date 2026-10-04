class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        max_profit = 0
        for price in prices:
            lowest = min(lowest, price)
            max_profit = max(max_profit, price - lowest)
        return max_profit