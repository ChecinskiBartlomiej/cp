#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l = prices[0]
        bg = 0
        for p in prices:
            if p < l:
                l = p
            g = p - l
            if p - l >= bg:
                bg = g
        return bg