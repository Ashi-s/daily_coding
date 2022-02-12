# Problen Link: https://leetcode.com/discuss/interview-question/347457/Amazon-or-OA-2019-or-Treasure-Island

# You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. 
# Other areas are safe to sail in. There are other explorers trying to find the treasure. 
# So you must figure out a shortest route to the treasure island.

# Assume the map area is a two dimensional grid, represented by a matrix of characters. 
# You must start from the top-left corner of the map and can move one block up, down, left or right at a time. 
# The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. 
# Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. 
# You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. 
# Output the minimum number of steps to get to the treasure.

# Example:

# Input:
# [['O', 'O', 'O', 'O'],
#  ['D', 'O', 'D', 'O'],
#  ['O', 'O', 'O', 'O'],
#  ['X', 'D', 'D', 'O']]

# Output: 5
# Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.

def treasure_island(grid):
  res = []
  helper(grid, res, 0, 0, [], [])
  return min(res) if len(res) > 0 else -1

def helper(grid, res, r, c, curr, visited):
  if grid[r][c] == 'X':
    res.append(sum(curr))
    return
  lst = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]

  for row, col in lst:
    if (row, col) not in visited:
      if row >= 0 and row < len(grid) and c >=0 and col < len(grid[0]) and grid[row][col] != 'D':
        curr.append(1)
        visited.append((row, col))
        helper(grid, res, row, col, curr, visited)
        curr.pop()
        visited.pop()
  
grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']]

print(treasure_island(grid))