def exist( board, word):
  def helper(r, c, curr):
    if len(curr) == len(word):
      if ''.join(curr) == word:
        res.append(word)
        return
      else:
        return
  
      
    lst = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]
    
    for row, col in lst:
      if row >= 0 and row < M and col >= 0 and col < N and (row, col) not in visited:
        curr.append(board[row][col])
        visited.append((row, col))
        helper(row, col, curr)
        
        curr.pop()
        visited.pop()
  res = []
  M = len(board)
  N = len(board[0])
  visited = []
  for i in range(M):
    for j in range(N):
      if board[i][j] == word[0]:
        visited = [(i, j)]
        helper(i, j, [board[i][j]])
  print(res)
  return True if len(res) > 0 else False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "SEE"
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "ABCB"
board3 = [["a","a"]]
word3 = "aaa"
board4 = [["C","A","A"],["A","A","A"],["B","C","D"]]
word4 = "AAB"
# print(exist(board, word))
# print(exist(board1, word1))
# print(exist(board2, word2))
# print(exist(board3, word3))
print(exist(board4, word4))




    