# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# https://www.youtube.com/watch?v=6X7Ha2PrDmM&ab_channel=NeetCode

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
      d = {}
      ROWS, COLS = len(matrix), len(matrix[0])
      
      self.helper(0,0, ROWS, COLS, matrix, d)
      return max(d.values()) ** 2

    def helper(self, r, c, ROWS, COLS, matrix, d):
      if r >= ROWS or c >= COLS:
        return 0
      
      if (r, c) not in d:
        right = self.helper(r, c+1, ROWS, COLS, matrix, d)
        down = self.helper(r+1, c, ROWS, COLS, matrix, d)
        diag = self.helper(r+1, c+1, ROWS, COLS, matrix, d)
        
        d[(r,c)] = 0
        if matrix[r][c] == '1':
          d[(r,c)] = 1 + min(right, down, diag)
          
      return d[(r,c)]