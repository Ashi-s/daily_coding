# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

from collections import deque

def orangesRotting(grid):
  fresh = 0
  q = deque()
  
  rows = len(grid)
  cols = len(grid[0])
  
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        fresh += 1
      elif grid[i][j] == 2:
        q.append((i, j , 0))
  print('q: ', q)    
  while q:
    r, c, t = q.popleft()
    lst = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]
    
    for row, col in lst:
      if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 1:
        q.append((row, col, t+1))
        fresh -= 1
        grid[row][col] = -1
  
        if fresh == 0:
          return t+1
  return 0 if fresh == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
grid1 = [[0,2]]
# print(orangesRotting(grid))
print(orangesRotting(grid1))