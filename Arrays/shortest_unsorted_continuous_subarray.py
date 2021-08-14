# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

# Input: nums = [1,2,3,4]
# Output: 0

def findUnsortedSubarray(nums):
  _min, _max = float('inf'), float('-inf')
      
  for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
      _min = min(_min, nums[i])
      
  for i in range(len(nums)-2, -1, -1):
    if nums[i] > nums[i+1]:
      _max = max(_max, nums[i])
  l = 0
  r = len(nums) - 1
  for i in range(len(nums)):
    if _min < nums[i]:
      break
    l += 1
  for i in range(len(nums)-1, -1, -1):
    if _max > nums[i]:
      break
    r -= 1
      
  return r - l +1 if r-l >= 0 else 0

# print(findUnsortedSubarray([1,3,2,2,2]))
print(findUnsortedSubarray([2,6,4,8,10,9,15]))
