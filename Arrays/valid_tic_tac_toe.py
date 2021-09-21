# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

# Example 1:

# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: "A" wins, he always plays first.
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"
# Example 2:

# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: "B" wins.
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
# "   "    "   "    "   "    "   "    "   "    "O  "
# Example 3:

# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# "XXO"
# "OOX"
# "XOX"
# Example 4:

# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
# "X  "
# " O "
# "   "
  
def tictactoe(moves):
  x_row = {0: [], 1:[], 2:[]}
  x_col = {0: [], 1:[], 2:[]}
  x_posDiagonal = []
  x_negDiagonal = []
  
  y_row = {0: [], 1:[], 2:[]}
  y_col = {0: [], 1:[], 2:[]}
  y_posDiagonal = []
  y_negDiagonal = []
  
  def check_winner(R, C, PD, ND, flag):
      for key, value in R.items():
        if sum(value) == 3:
          return flag
      for key, value in C.items():
        if sum(value) == 3:
          return flag
      if sum(PD) == 3:
        return flag
      if sum(ND) == 3:
        return flag
    
      return "NO"
    
  for m in range(len(moves)):
    r, c = moves[m][0], moves[m][1]
    
    if m % 2 == 0:
      x_row[r].append(1)
      x_col[c].append(1)
      
      #pos diagonal
      if r+c == 2:
        x_posDiagonal.append(1)
      #neg diagonal
      if r-c == 0:
        x_negDiagonal.append(1)
    else:
      y_row[r].append(1)
      y_col[c].append(1)
      
      #pos diagonal
      if r+c == 2:
        y_posDiagonal.append(1)
      #neg diagonal
      if r-c == 0:
        y_negDiagonal.append(1)
    
    
    X = check_winner(x_row, x_col, x_posDiagonal, x_negDiagonal, flag="A")
    Y = check_winner(y_row, y_col, y_posDiagonal, y_negDiagonal, flag="B")
    
    if X != "NO":
      return X
    elif Y != "NO":
      return Y
  
  if len(moves) == 9:
    return "Draw"
  else:
    return "Pending"
  
    
print(tictactoe(moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(tictactoe(moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(tictactoe(moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(tictactoe(moves = [[0,0],[1,1]]))


      
    
  
    