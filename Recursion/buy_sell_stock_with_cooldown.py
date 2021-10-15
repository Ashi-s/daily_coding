# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0

#M1 basic recursion
def maxProfit(prices):

  def helper(res, idx, profit, buy):
    if idx >= len(prices):
      res.append(profit)
      return
    
    #buy
    if buy:
      helper(res, idx+1, profit - prices[idx], False)
    #sell
    else:
      helper(res, idx+2, profit + prices[idx], True)
    
    #cooldown
    helper(res, idx+1, profit, buy)
    
  res = []
  helper(res, 0, 0, True)
  return max(res)

#M2 DP
# https://www.youtube.com/watch?v=I7j0F7AHpb8&ab_channel=NeetCode
def maxProfit(prices):
  #dp = {(i, buying)} (index, boolean)
  dp = {}
  def helper(idx, buying):
    if idx >= len(prices):
      return 0
    
    if (idx, buying) in dp:
      return dp[(idx, buying)]
    
    cooldown = helper(idx+1, buying)
    #buying
    if buying:
      buy = helper(idx+1, not buying) - prices[idx]
      dp[(idx, buying)] = max(buy, cooldown)
    #sell
    else:
      sell = helper(idx+2, not buying) + prices[idx]
      dp[(idx, buying)] = max(sell, cooldown)
    
    return dp[(idx, buying)]
  
  return helper(0, True)