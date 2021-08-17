
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

def change( amount, coins):
  dp = [[] for i in range(amount+1)]
  
  for c in coins:
    for i in range(1, amount+1):
      if i-c < 0:
        continue
      elif i-c == 0:
        dp[i].append([c])
      else:
        for li in dp[i-c]:
          dp[i].append(li+[c])
  return len(dp[-1])

print(change(amount = 5, coins = [1,2,5]))
        