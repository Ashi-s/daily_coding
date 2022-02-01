# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#M1
def buy_stock(prices):
  max_profit = 0
  buy = float('inf')

  for each in prices:
    buy = min(buy, each)
    profit = each - buy
    max_profit = max(max_profit, profit)

  return max_profit

#M2
class Solution:
    def maxProfit(prices):
      if len(prices) <= 1:
        return 0
      if len(prices) == 2:
        if prices[1] < prices[0]:
          return 0
        else:
          return prices[1] - prices[0]
      
      profit = 0
      min_value = float('inf')
      for i in prices:
        if i < min_value:
          min_value = i
        elif i - min_value > profit:
          profit = i - min_value
      
      return profit
print(buy_stock([7,1,5,3,6,4]))