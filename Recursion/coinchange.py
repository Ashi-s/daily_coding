#input coins = [1, 2, 5] , amount = 11
# output = 3 (min coins)
# https://www.youtube.com/watch?v=1R0_7HqNaW0&ab_channel=KevinNaughtonJr.

def coin_change(coins, amount):
  dp = [amount+1] * (amount+1)

  dp[0] = 0

  for i in range(amount + 1):
    for j in coins:
      if i-j >= 0:
        dp[i] = min(dp[i], 1+dp[i-j])
  if dp[amount] != amount+1:
    return dp[amount]
  else:
   return -1
print(coin_change([1,2,5], 11))

