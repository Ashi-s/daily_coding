# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
# Example 2:

# Input: grid = [[1,1],[1,0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
# Example 3:

# Input: grid = [[1,1],[1,1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.

####IMP this code runs correct when just one input is passed, if you want result for multiple input it will give wrong result because of the global variable
#### therefore add output_max = 1 after each test input(look line 49)
output_max = 1
def making_a_large_island(grid):
  res = 0
  
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 0:
        dfs(grid.copy(), i, j , 1)
  return output_max

def dfs(mat, row, col, count):
  lst = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

  for r, c in lst:
    if r>=0 and r<len(mat) and c >= 0 and c < len(mat[0]) and mat[r][c] == 1:
      mat[r][c] = 0
      count += 1
      global output_max
      if count > output_max:
        output_max = count
      dfs(mat, r, c, count)
  

print(making_a_large_island([[1,1],[1,0]]))
output_max = 1
print(making_a_large_island([[0,0],[0,0]]))