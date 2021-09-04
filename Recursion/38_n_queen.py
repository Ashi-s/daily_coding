# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above


def solveNQueens(n):
  res = []
  board = [["."]*n for _ in range(n)]
  
  cols = set()
  positive_diagonal = set() #r+c is constant
  negative_diagonal = set() #r-c is constant
  
  helper(res, board, n , 0, cols, positive_diagonal, negative_diagonal)
  return res
      

def helper(res, board, n , row, cols, positive_diagonal, negative_diagonal):
  if row == n:
    copy = ["".join(i) for i in board]
    res.append(copy)
    return
  
  #loop through cols
  for c in range(n):
    if c in cols or (row+c) in positive_diagonal or (row-c) in negative_diagonal:
      continue
    
    cols.add(c)
    positive_diagonal.add(row+c)
    negative_diagonal.add(row-c)
    board[row][c] = "Q"
    
    helper(res, board, n, row+1, cols, positive_diagonal, negative_diagonal)
    
    cols.remove(c)
    positive_diagonal.remove(row+c)
    negative_diagonal.remove(row-c)
    board[row][c] = "."
        
print(solveNQueens(4))