# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return the number of maximum integers in the matrix after performing all the operations.

 

# Example 1:


# Input: m = 3, n = 3, ops = [[2,2],[3,3]]
# Output: 4
# Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
# Example 2:

# Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
# Output: 4
# Example 3:

# Input: m = 3, n = 3, ops = []
# Output: 9

#METHOD 1 : MAX TIME EXCEEDED
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

      mat = [[0 for _ in range(m)] for _ in range(n)]
      d = {0: m*n}
      
      for x, y in ops:
        for i in range(x):
          for j in range(y):
            val = mat[i][j]
            if val+1 not in d:
              d[val + 1] = 1
            else:
              d[val+1] += 1
            d[val] -= 1
            mat[i][j] += 1
      max_key = max(d.keys())
      return d[max_key]
        
#METHOD 2
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
      min_row = m
      min_col = n
      
      for r, c in ops:
        min_row = min(min_row, r)
        min_col = min(min_col, c)
        
      return min_row * min_col