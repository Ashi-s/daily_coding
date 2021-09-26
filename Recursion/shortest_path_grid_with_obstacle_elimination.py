# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:

# Input: 
# grid = 
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 
# k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:

# Input: 
# grid = 
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]], 
# k = 1
# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.

def shortest_path(grid, k):
  res = []
  M = len(grid) - 1
  N = len(grid[0]) - 1

  helper(grid, res, 0, 0, M, N, [], [], k)
  print(res)
  return min(res) if len(res) > 0 else -1

def helper(grid, res, row, col, M, N, curr, visited, k):
  #base case
  if row == M and col == N:
    res.append(sum(curr))
    return
  
  if row > M or col > N:
    return

  lst = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

  for r, c in lst:
    if r >= 0 and r <= M and c >= 0 and c <= N and (r,c) not in visited:
      if k > 0 and grid[r][c] == 1:
        visited.append((r,c))
        curr.append(1)
        helper(grid, res, r, c, M, N, curr, visited, k-1)
        visited.pop()
        curr.pop()
      elif grid[r][c] == 0:
        visited.append((r,c))
        curr.append(1)
        helper(grid, res, r, c, M, N, curr, visited, k)
        visited.pop()
        curr.pop()

grid = [[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]]

grid1 = [[0,0], [1,0]]

grid2 = [[0,1,1],
 [1,1,1],
 [1,0,0]]

grid3 = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
print(shortest_path(grid, 1))
print(shortest_path(grid1, 1))
print(shortest_path(grid2, 1))
print(shortest_path(grid3, 1))
