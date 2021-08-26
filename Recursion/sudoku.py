# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.

# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.

# Implement an efficient sudoku solver.


def solveSudoku():
    """
    Do not return anything, modify board in-place instead.
    """
    global board
    for r in range(9):
      for c in range(9):
        if board[r][c] == '.':
          for k in range(1, 10):
            if is_possible(r, c, k):
              board[r][c] = str(k)
              solveSudoku()
              board[r][c] = '.'
          return
    print(board)

        
        
        
def is_possible(row, col, number):
  global board
  
  #check row
  for i in range(9):
    if (board[row][i]) == str(number):
      return False
  
  # check column
  for i in range(9):
    if (board[i][col]) == str(number):
      return False
  
  # check 3x3 matrix
  x0 = (col // 3) * 3
  y0 = (row // 3) * 3
  for i in range(3):
    for j in range(3):
      if (board[y0+i][x0+j]) == str(number):
        return False
  return True
        
board = [
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
print(solveSudoku())
