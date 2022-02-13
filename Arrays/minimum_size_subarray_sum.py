# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
# of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

def minSubArrayLen(target, nums):
  left = 0
  _min = float('inf')
  summ = 0
  
  for right in range(len(nums)):
    summ += nums[right]
    
    while summ >= target:
      _min = min(_min, right-left+1)
      summ -= nums[left]
      left += 1
  
  return _min if _min != float('inf') else 0
            