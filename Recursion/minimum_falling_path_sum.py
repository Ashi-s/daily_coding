# https://www.youtube.com/watch?v=Xr_LRdr9IPQ&ab_channel=CodeNCode

# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum underlined below:
# [[2,1,3],      [[2,1,3],
#  [6,5,4],       [6,5,4],
#  [7,8,9]]       [7,8,9]]

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
      if len(matrix) == 1:
        return min(matrix[0])
      dp = []
      for i in range(len(matrix)-1):
        dp.append([0]*len(matrix[0]))
      dp.append(matrix[-1])
      
      for row in range(len(matrix)-2, -1, -1):
        for col in range(len(matrix[0])):
          helper(row, col, dp, matrix)
      return min(dp[0])
          
def helper(row, col, dp, matrix):
  minimum = dp[row+1][col]
  if col-1 >= 0:
    minimum = min(minimum, dp[row+1][col-1])
  if col+1 < len(matrix[0]):
    minimum = min(minimum, dp[row+1][col+1])
  dp[row][col] = matrix[row][col] + minimum