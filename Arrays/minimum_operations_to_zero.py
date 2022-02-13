
# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or 
# the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
# Example 2:

# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# Example 3:

# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


# template similar to LC 209 Minimum Size Subarray Sum


def minOperations( nums, x):
  left = 0
  _max = -1
  summ = 0
  target = sum(nums) - x
  
  if target < 0: return -1
  if target == 0: return len(nums)
  
  for right in range(len(nums)):
    summ += nums[right]
    
    while summ >= target:
      if summ == target:
        _max = max(_max, right-left+1)
      
      summ -= nums[left]
      left += 1
  return len(nums)-_max if _max != -1 else -1

#M1 Recursion TLE
#       def helper(nums, curr, res, count):
#         if curr == x:
#           res.append(count)
#           return
        
#         if curr > x:
#           return
        
#         helper(nums[1:], curr+nums[0], res, count+1)
#         helper(nums[:len(nums)-1], curr+nums[-1], res, count+1)
#         helper(nums[1:len(nums)-1], curr+nums[0]+nums[-1], res, count+2)
      
#       if sum(nums) == x:
#         return len(nums)
#       elif sum(nums) < x:
#         return -1
      
#       res = []
#       helper(nums, 0, res, 0)
      
#       return min(res) if len(res) > 0 else -1