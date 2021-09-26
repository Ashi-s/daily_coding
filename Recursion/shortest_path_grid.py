# Input: 
# grid = 
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]], 

# Output: 10
# Explanation: 
# The shortest path without eliminating any obstacle is 10. 

# Example 2:

# Input: 
# grid = 
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]], 

# Output: -1
# Explanation: 
# We need to eliminate at least two obstacles to find such a walk.

def shortest_path(grid):
  res = []
  M = len(grid) - 1
  N = len(grid[0]) - 1

  helper(grid, res, 0, 0, M, N, [], [])
  print(res)
  return min(res) if len(res) > 0 else -1

def helper(grid, res, row, col, M, N, curr, visited):
  #base case
  if row == M and col == N:
    res.append(sum(curr))
    return
  
  if row > M or col > N:
    return

  lst = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

  for r, c in lst:
    if r >= 0 and r <= M and c >= 0 and c <= N and grid[r][c] == 0 and (r,c) not in visited:
      visited.append((r,c))
      curr.append(1)
      helper(grid, res, r, c, M, N, curr, visited)
      visited.pop()
      curr.pop()

grid = [[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]]

grid1 = [[0,0], [1,0]]
print(shortest_path(grid))