# https://www.youtube.com/watch?v=OM1MTokvxs4&ab_channel=NeetCode
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

def minimumTotal(triangle):
  dp = [0] * (len(triangle)+1)
  
  for row in triangle[::-1]:
    for i, v in enumerate(row):
      dp[i] = v + min(dp[i], dp[i+1])
  return dp[0]