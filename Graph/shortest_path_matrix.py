# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 
def shortestPathBinaryMatrix(grid):
  def helper(r, c, curr, visited):
      nonlocal result
      if r == X-1 and c == Y-1:
          result = min(result, curr)
          return
      if r > X or c > Y:
          return
      lst = [(r, c+1), (r, c-1), (r+1, c), (r-1, c), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1)]
      for row, col in lst:
          if row >= 0 and row < X and col >= 0 and col < Y and grid[row][col] == 0 and (row, col) not in visited:
              visited.append((row, col))
              helper(row, col, curr+1, visited)
              visited.pop()
  
  if grid[0][0] == 1:
    return -1
  
  X, Y = len(grid), len(grid[0])
  result = float('inf')
  visited = []
  visited.append((0,0))
  helper(0, 0, 1, visited)
  return result if result != float('inf') else -1

grid = [
  [0,0,0],
  [1,1,0],
  [1,1,0]]

grid1 = [
  [0,0,0],
  [1,0,0],
  [1,1,0]]

# print(shortestPathBinaryMatrix(grid))
print(shortestPathBinaryMatrix(grid1))
