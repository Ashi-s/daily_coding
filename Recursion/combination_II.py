# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]


def combinationSum2(s, target):
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
      if i != index and c == s[i-1]: continue 
      helper(res, s, target-c, i+1, current+[c])