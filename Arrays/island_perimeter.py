# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:
# Input: grid = [[1]]
# Output: 4

# Example 3:
# Input: grid = [[1,0]]
# Output: 4
def islandPerimeter(grid):
      
  def check_sides(i, j, row, col):
    tmp = 4
    #check left
    if j-1 >= 0 and j-1 < col and grid[i][j-1] == 1:
      tmp -= 1
    #check right
    if j+1 >= 0 and j+1 < col and grid[i][j+1] == 1:
      tmp -= 1
    #check up
    if i-1 >= 0 and i-1 < row and grid[i-1][j] == 1:
      tmp -= 1
    #check down
    if i+1 >= 0 and i+1 < row and grid[i+1][j] == 1:
      tmp -= 1
    return tmp
        
    
  perimeter = 0
  row = len(grid)
  col = len(grid[0])
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        val = check_sides(i, j, row, col)
        perimeter += val
  return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(grid))