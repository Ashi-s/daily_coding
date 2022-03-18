import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def findPositions(arr, x):
  # Write your code here
  q = deque([(n,i+1) for i,n in enumerate(arr)])
  ret = []
  
  for _ in range(x):
    mx = float('-inf')
    popped = []
    
    j = 0
    while q and j < x:
      n,i = q.popleft()
      if n > mx:
        mx = n
        mxj = j
        mxi = i
      popped.append((max(0, n-1), i))
      j += 1
      
      
    if popped:
      popped.pop(mxj)
    if popped:
      q.extend(popped)
    
    ret.append(mxi)
    
  return ret

arr = [1, 2, 2, 3, 4, 5]
x = 5

print(findPositions(arr, x))