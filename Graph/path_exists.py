# Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
# Note: You can only move left, right, up and down, and only through cells that contain 1.

# Example 1:

# Input:
# N=3
# M=4
# A=[[1,0,0,0], 
# [1,1,0,1],[0,1,1,1]]
# X=2
# Y=3 
# Output:
# 5
# Explanation:
# The shortest path is as follows:
# (0,0)->(1,0)->(1,1)->(2,1)->(2,2)->(2,3).
# Example 2:

# Input:
# N=3
# M=4
# A=[[1,1,1,1],
# [0,0,0,1],[0,0,0,1]]
# X=0
# Y=3
# Output:
# 3
# Explanation:
# The shortest path is as follows:
# (0,0)->(0,1)->(0,2)->(0,3).


def is_Possible( grid):
  #Code here
  def helper(source, destination, visited):
      nonlocal isPath
      print(source, destination)
      # if source == destination:
      #     isPath = True
      r,c = source
      lst = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]
      
      for row, col in lst:
          if row >= 0 and row < n and col >= 0 and col < m and (row, col) not in visited:
              if grid[row][col] == 3:
                visited.add((row, col))
                helper((row, col), destination, visited)
                visited.pop()
              elif grid[row][col] == 2:
                isPath = True
                return
  
  
  isPath = False
  n, m = len(grid), len(grid[0])
  visited = set()
  for i in range(n):
      for j in range(m):
          if grid[i][j] == 1:
              source = (i, j)
          if grid[i][j] == 2:
              destination = (i, j)
  
  visited.add(source)
  helper(source, destination, visited)
  return isPath


grid = [
  [1,3],
  [3,2]
]
print(is_Possible(grid))