#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        price_min = 10000  # 최저 주식값
        profit = 0  # 수익

        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current - price_min)
        return profit