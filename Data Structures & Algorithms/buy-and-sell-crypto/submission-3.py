class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 100
        potential = 100
        sell_price = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < potential:
                potential = prices[i]
            elif prices[i] > potential and max(prices[i] - potential, 0) > profit:
                sell_price = prices[i]
                buy_price = potential
                profit = max(sell_price - buy_price, 0)
        return profit