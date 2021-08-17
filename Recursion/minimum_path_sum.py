def min_path_sum(grid):
  res = []
  helper(grid, res, 0, 0, 0, len(grid), len(grid[0]))
  return min(res)

def helper(grid, res, i, j , count, rows, cols):
  if i == rows-1 and j == cols-1:
    res.append(count+grid[i][j])
    return
  if i >= rows or j >= cols:
    return
  
  count += grid[i][j]
  print(i, j, grid[i][j], count)
  
  helper(grid, res, i, j+1 , count, rows, cols)
  helper(grid, res, i+1, j , count, rows, cols)
  print('res: ', res)

# print(min_path_sum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
# print(min_path_sum(grid = [[1,2,3],[4,5,6]]))

# Bottom up approach
# https://www.youtube.com/watch?v=pGMsrvt0fpk&ab_channel=NeetCode

def min_path_sum(grid):
  rows, cols = len(grid), len(grid[0])
  res = [[float('inf')]*(cols+1) for r in range(rows+1)]
  res[rows][cols-1] = 0

  for r in range(rows-1, -1, -1):
    for c in range(cols-1, -1, -1):
      res[r][c] = grid[r][c] +  min(res[r+1][c], res[r][c+1])
  print(res)
  return res[0][0]

print(min_path_sum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(min_path_sum(grid = [[1,2,3],[4,5,6]]))