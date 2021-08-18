'''
 n = 5 e = [[0,1], [1, 2], [3, 4] ]
 output = 2
 0 -- 1  3 -- 4
      |
      2

'''

def num_connected(n, edges):
  d = {}
  visited = set()
  count = 0
  for e in edges:
    u, v = e[0], e[1]
    if u not in d:
      d[u] = [v]
    else:
      d[u].append(v)
    if v not in d:
      d[v] = [u]
    else:
      d[v].append(u)
  print(d)
  for i in range(n):
    if i not in visited:
      count += 1
      dfs(i, visited, d)
  return count

def dfs(i, visited, d):
  visited.add(i)
  for each in d[i]:
    if each not in visited:
      dfs(each, visited, d)

print(num_connected(5, [[0,1], [1, 2], [3, 4]]))
