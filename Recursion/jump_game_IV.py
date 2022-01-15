# Given an array of integers arr, you are initially positioned at the first index of the array.

# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
# Example 2:

# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
# Example 3:

# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.


##### Method 1 (Recursion) TLE
def jump_game_IV(arr):
  N = len(arr)
  d = {}

  if len(arr) < 2:
    return 0

  for i in range(N):
    if arr[i] not in d:
      d[arr[i]] = [i]
    else:
      d[arr[i]].append(i)


  def helper(idx, count, res, visited):
    if idx == N-1:
      res.append(count)
      return

    if idx-1 >= 0:
      if idx-1 not in visited:
        visited.add(idx-1)
        helper(idx-1, count+1, res, visited)
        visited.remove(idx-1)

    if idx+1 < N:
      if idx+1 not in visited:
        visited.add(idx+1)
        helper(idx+1, count+1, res, visited)
        visited.remove(idx+1)

    if d[arr[idx]]:
      for each in d[arr[idx]]:
        if each != idx and each not in visited:
          visited.add(each)
          helper(each, count+1, res, visited)
          visited.remove(each)

  res = []
  visited = set()
  helper(0, 0, res, visited)

  return min(res)


##### Method 2 (BFS)
def minJumps(arr):
  visited = {0}
  curr = [0]
  N = len(arr)
  d = {}
  count = 0
  if len(arr) < 2:
    return 0
  
  for i in range(N):
    if arr[i] not in d:
      d[arr[i]] = [i]
    else:
      d[arr[i]].append(i)
  
  while curr:
    nex = []
    for node in curr:
      if node == N-1:
        return count

      for i in d[arr[node]]:
        if i not in visited:
          nex.append(i)
          visited.add(i)
      
      d[arr[node]].clear()
      
      for i in [node-1, node+1]:
        if 0<=i<N and i not in visited:
          nex.append(i)
          visited.add(i)
    
    curr = nex
    count += 1
  
  return -1
            
        

print(jump_game_IV([7,6,9,6,9,6,9,7]))
print(jump_game_IV([100,-23,-23,404,100,23,23,23,3,404]))
