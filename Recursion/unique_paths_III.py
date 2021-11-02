# You are given an m x n integer array grid where grid[i][j] could be:

# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

# Example 1:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:


# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

def uniquePathsIII(grid):
      
  def dfs(r, c, count):
    if grid[r][c] == 2 and count == non_obstacles:
      res.append(1)
      return
    lst = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]
    
    for row, col in lst:
      if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] != -1 and seen[row][col] != 1:
        seen[row][col] = 1
        dfs(row, col, count+1)
        seen[row][col] = 0
  rows = len(grid)
  cols = len(grid[0])
  seen = [[0]*cols for _ in range(rows)]
  
  non_obstacles = 0
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 0 or grid[i][j] == 2:
        non_obstacles += 1
      if grid[i][j] == 1:
        start = (i, j)
        seen[i][j] = 1
  
  res = []
  dfs(start[0], start[1], 0)
  return sum(res)

grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
print(uniquePathsIII(grid))