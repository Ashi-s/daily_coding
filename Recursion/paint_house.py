# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least. Return the minimum cost.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
# For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

# Input: [[14,2,11],[11,14,5],[14,3,10]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.

def paint_house(nums):
  n = len(nums)
  # dp = [nums[0]]
  # dp.extend([[0] * 3 ] * (n-1))
  dp = [nums[0], [0,0,0], [0,0,0]]

  for i in range(1, len(nums)):
    print(dp)
    dp[i][0] = nums[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = nums[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = nums[i][2] + min(dp[i-1][0], dp[i-1][1])
  print(dp)
  return min(dp[n-1])

print(paint_house([[14,2,11],[11,14,5],[14,3,10]]))
