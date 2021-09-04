# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1

class Solution:
    def totalNQueens(self, n: int) -> int:
      board = [['.']*n for _ in range(n)]
      res = []
      cols = set()
      pos_diagonal = set()
      neg_diagonal = set()
      
      helper(res, board, n , 0, cols, pos_diagonal, neg_diagonal)
      return len(res)
    
def helper(res, board, n, row, cols, pos_diagonal, neg_diagonal):
  if row == n:
    copy = [''.join(i) for i in board]
    res.append(copy)
    return
    
  
  for c in range(n):
    if c in cols or (row+c) in pos_diagonal or (row-c) in neg_diagonal:
      continue
    
    cols.add(c)
    pos_diagonal.add(row+c)
    neg_diagonal.add(row-c)
    board[row][c] = 'Q'
    
    helper(res, board, n, row+1, cols, pos_diagonal, neg_diagonal)
    
    cols.remove(c)
    pos_diagonal.remove(row+c)
    neg_diagonal.remove(row-c)
    board[row][c] = '.'