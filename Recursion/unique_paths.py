# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
# Example 3:

# Input: m = 7, n = 3
# Output: 28
# Example 4:

# Input: m = 3, n = 3
# Output: 6

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      dp = [[1]*n] * m
      
      for i in range(1, m):
        for j in range(1, n):
          dp[i][j] = dp[i-1][j] + dp[i][j-1]
      return dp[m-1][n-1]
#     Using recursion 
#         self.count = 0
#         def dfs(r, c):
#           lst = [(r, c+1), (r+1, c)]

#           if r == m-1 and c == n-1:
#             self.count += 1
#             return

#           if r > m-1 or c > n-1:
#             return

#           for r, c in lst:
#             if r < m and c < n:
#               dfs(r, c)
#         dfs(0, 0)
#         return self.count

    