# This problem was asked by Google.

# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

# Integers can appear more than once in the list. You may assume all numbers in the list are positive.

# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

### METHOD 1 (Time Limit Exceed) 
# but to understand the recusrion, first try solving this way 
# and draw the recursion graph on the paper
def subset_target(s, target):
  res = []
  helper(res, s, target, 0, [])
  return res

def helper(res, s, target, index, current):
  if sum(current) == target:
    current.sort()
    if current not in res:
      res.append(current.copy())
    return
  
  if sum(current) > target:
    return
  
  if index == len(s):
    return

  current.append(s[index])
  helper(res, s, target, index+1, current)

  current.pop()
  helper(res, s, target, index+1, current)

# print(subset_target([12, 1, 61, 5, 9, 2], 24))
# print(subset_target([10,1,2,7,6,1,5], target = 8))


### METHOD 2
def subset_target_2(s, target):
  res = []
  s.sort()
  helper(res, s, target, 0, [])
  return res

def helper(res, s , target, index, current):
  if target < 0:
    return
  
  if target == 0:
    res.append(current)
    return

  if target > 0:
    for i in range(index, len(s)):
      c = s[i]
      # current.append(s[i])
      if i != index and c == s[i-1]: continue 
      helper(res, s, target-c, i+1, current+[c])

print(subset_target_2([12, 1, 61, 5, 9, 2], 24))
# print(subset_target_2([10,1,2,7,6,1,5], target = 8))

def combinationSum2(candidates, target):
  candidates.sort()
  res = []
  
  def dfs(t, idx=0, path=[]):
      if t < 0:
          return  # Backtrack (Not a valid path)
      
      if t == 0:
          res.append(path)
          return
      
      if t > 0:
          for i in range(idx, len(candidates)):
              c = candidates[i]
              if i != idx and c == candidates[i-1]: continue  # Eliminates duplicates
              dfs(t-c, i+1, path+[c])

  dfs(target)
  return res

print(combinationSum2([12, 1, 61, 5, 9, 2], 24))

