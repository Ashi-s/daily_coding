# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def combine(n, k):
  result = []
  helper(result, n, k, 1, [])
  return result
    
def helper(result, n, k, index, current):
  if len(current) == k:
      result.append(current.copy())
      return
  
  for i in range(index, n+1):
      current.append(i)
      helper(result, n, k, i+1, current)
      current.pop()

print(combine(4, 2))