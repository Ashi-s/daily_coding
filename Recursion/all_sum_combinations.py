# The goal of this exercise is to use your backtracking skills to find all sum combinations.

# Problem statement: Given a positive integer, target, print all possible combinations of positive integers that add to the target number.

# The output will be in the form a list of lists or an array of arrays, as each element in the list will be another list containing a possible sum combination.

def all_combinations(target):
  res = []
  helper(1, target, [], res)
  return res

def helper(start, target, curr, res):
  if sum(curr) == target:
    res.append(curr.copy())
    return
  
  if sum(curr) > target:
    return
  
  for i in range(start, target+1):
    curr.append(i)
    helper(start, target, curr, res)
    curr.pop()

print(all_combinations(5))