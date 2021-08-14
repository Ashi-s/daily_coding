# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}

def power_Set(s):
  res = [[]]
  helper(res, s, 0, [])
  return res

def helper(res, s, index, current):
  if index >= len(s):
    return

  for i in s[index:]:
    current.append(i)
    res.append(current.copy())
    helper(res, s, index+1, current)
    current.pop()
    index += 1 ##imp run it in debug mode to understand it better

print(power_Set([1,2,3]))