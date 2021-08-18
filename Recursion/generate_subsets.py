
# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 # Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def generate_subsets(nums):
  if len(nums) == 0:
    return []

  result = []

  helper(result, nums, 0, [])
  return result

def helper(result, nums, index, current):
  if index == len(nums):
    result.append(current.copy())
    return
  #Add
  current.append(nums[index])
  helper(result, nums, index+1, current)

  #not Add
  current.pop()
  helper(result, nums, index+1, current)
print(generate_subsets([1,2,3]))