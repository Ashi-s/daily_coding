# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def buy_stock(prices):
  max_profit = 0
  buy = float('inf')

  for each in prices:
    buy = min(buy, each)
    profit = each - buy
    max_profit = max(max_profit, profit)

  return max_profit

print(buy_stock([7,1,5,3,6,4]))