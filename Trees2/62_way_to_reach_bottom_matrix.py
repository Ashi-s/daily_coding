count = 0
def numberWaysTopToBottom(N, M):
  global count
  def dfs(r, c):
    global count
    lst = [(r, c+1), (r+1, c)]

    if r == N-1 and c == M-1:
      count += 1
      return
    
    if r > N-1 or c > M-1:
      return
    
    for r, c in lst:
      if r < N and c < M:
        dfs(r, c)
  
  dfs(0, 0)
  return count

print(numberWaysTopToBottom(3, 7))