# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Input = [[2,1,1],[0,1,1],[1,0,1]]
# output = -1


def orangesRotting(grid):
  fresh = 0
  minutes = 0
  #count fresh
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if grid[row][column] == 1:
        fresh += 1
        
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if grid[row][column] == 2 and should_continue(grid, row, column):
        fresh = dfs(row, column, grid, fresh)
        minutes += 1
  
  return minutes if fresh == 0 else -1

def should_continue(grid, row, column):
  lst = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
  val = 0    
  for r,c in lst:
    if r >=0 and r<len(grid) and c >= 0 and c < len(grid[r]) and grid[r][c] == 1:
      val += 1
  return val

def dfs(row, column, grid, fresh):
  lst = [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]
  for r,c in lst:
    if r >=0 and r<len(grid) and c >= 0 and c < len(grid[r]) and grid[r][c] == 1:
      grid[r][c] = 2
      fresh -= 1
  return fresh

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
