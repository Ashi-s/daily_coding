# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

 

# Example 1:


# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:


# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

def gameOfLife(board):
  """
  Do not return anything, modify board in-place instead.
  """
  m, n = len(board), len(board[0])
  grid = [[0] * n for _ in range(m)]
  
  def helper(r, c):
    lst = [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1)]
    
    tmp = 0
    for row, col in lst:
      if row >= 0 and row < m and col >= 0 and col < n and board[row][col] == 1:
        tmp += 1
    
    if board[r][c] == 1:
      if tmp < 2: #case1
        grid[r][c] = 0
      elif tmp in [2, 3]:#case2
        grid[r][c] = 1
      elif tmp > 3:#case3
        grid[r][c] = 0
    #case 4
    elif board[r][c] == 0 and tmp == 3:
      grid[r][c] = 1
      
  
  for i in range(m):
    for j in range(n):
      helper(i, j)
  
  for i in range(m):
    for j in range(n):
      board[i][j] = grid[i][j]
  return board

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
print(gameOfLife(board))