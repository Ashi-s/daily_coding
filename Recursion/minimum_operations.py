# Given a number N. Find the minimum number of operations required to reach N starting from 0. You have 2 operations available:

# Double the number
# Add one to the number

# Example 1:

# Input:
# N = 8
# Output: 4
# Explanation: 0 + 1 = 1, 1 + 1 = 2,
# 2 * 2 = 4, 4 * 2 = 8


def minOperation(n):
  # code here 
  result = 0
  def helper(curr, count):
      nonlocal result
      if curr == 0:
          print(count)
          result = count
          return
      if curr % 2 != 0:
        helper(curr-1, count+1)
      else:
        helper(curr//2, count+1)
      
  
  
  helper(n, 0)
  return result

print(minOperation(5))