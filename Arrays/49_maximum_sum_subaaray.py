# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

def maxSubArray(self, nums: List[int]) -> int:
  maxSum = float('-inf')
  summed = 0
  
  for each in nums:
    summed += each
    maxSum = max(maxSum, summed)
    
    if summed < 0:
      summed = 0
  return maxSum