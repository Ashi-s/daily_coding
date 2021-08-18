# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

def num_islands(grid):
  if len(grid) == 0:
    return 0

  num_of_islands = 0

  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if grid[row][column] == '1':
        num_of_islands += 1
        dfs(row, column, grid)

  return num_of_islands

def dfs(row, column, grid):
  grid[row][column] = '0'
  lst = [(row -1, column), (row+1, column), (row, column+1), (row, column-1)]

  for r, c in lst:
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]) and grid[r][c] != '0':
      dfs(r, c, grid)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(num_islands(grid))