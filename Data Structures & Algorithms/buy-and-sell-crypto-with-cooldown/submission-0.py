class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        held = -prices[0]
        rest = 0
        sold = 0

        for i in range(1,len(prices)):

            prev_sold = sold

            sold = held+prices[i]
            held = max(rest-prices[i],held)
            rest = max(rest,prev_sold)

        return max(rest,sold)
