class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0

        while i < len(prices) - 1:
            if prices[i] < prices[i + 1]:
                startPrice = prices[i]

                while i < len(prices) - 1 and prices[i] < prices[i + 1]:
                    i = i + 1

                endPrice = prices[i]
                profit = profit + endPrice - startPrice

            i = i + 1

        return profit
