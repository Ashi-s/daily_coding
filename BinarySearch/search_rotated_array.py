# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def search(nums, target):
  if len(nums) == 0:
    return 0
  n = len(nums) 
  i = n // 2
  j = n// 2 + 1

  for k in range(n//2 + 1):
    if nums[i] == target:
      return i
    if j < len(nums) and nums[j] == target:
      return j
    j += 1
    i -= 1
  return -1
print(search( nums = [4,5,6,7,0,1,2], target = 0))
print(search( nums = [4,5,6,7,0,1,2], target = 3))