# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []

# Solution 1: Recursion

# def threeSum(nums):
#   def helper(res, idx, curr):
#     if len(curr) == 3:
#       if sum(curr) == 0:
#         tmp = curr.copy()
#         tmp.sort()
#         if tmp not in res: res.append(tmp)
#       return
    
#     if idx >= len(nums):
#       return
#     curr.append(nums[idx])
#     helper(res, idx+1, curr)
    
#     curr.pop()
#     helper(res, idx+1, curr)
  
#   res = []
#   helper(res, 0, [])
#   return res


def threeSum(nums):
  res = []
  nums.sort()
  for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    left = i + 1
    right = len(nums) - 1
    
    while left < right:
      amount = nums[i] + nums[left] + nums[right]
      if amount == 0:
        res.append([ nums[i], nums[left], nums[right]])
        while left < right and nums[left] == nums[left+1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1
      elif amount > 0:
        right -= 1
      elif amount < 0:
        left += 1
    
  return res
        
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))