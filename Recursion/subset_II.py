# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 

# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]


def subsetsWithDup(nums):
  res = []
  helper(res, nums, 0, [])
  return res
    
def helper(res, nums, index, current):
  if index == len(nums):
    temp = current.copy()
    temp.sort()
    if temp not in res:
      res.append(temp)
    return
  
  current.append(nums[index])
  helper(res, nums, index+1, current)
  
  current.pop()
  helper(res, nums, index+1, current)