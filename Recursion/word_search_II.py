def exist( board, words):
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
  for word in words:
    for i in range(M):
      for j in range(N):
        if board[i][j] == word[0]:
          visited = [(i, j)]
          helper(i, j, [board[i][j]])
  print(res)
  return list(set(res))

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
board1 = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words1 = ["oa","oaa"]
print(exist(board, words))
print(exist(board1, words1))





    