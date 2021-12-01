# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Input: nums = [1,3,5,6], target = 0
# Output: 0

# Input: nums = [1], target = 0
# Output: 0


def searchInsert(nums, target):
  left = 0
  right = len(nums) - 1
    
  while left <= right:
    mid = (left+right) // 2
    
    if nums[mid] == target:
      return mid
    elif nums[mid] > target:
      right = mid - 1
    elif nums[mid] < target:
      left = mid + 1
      
  return left

print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert([1,3,5,6], target = 2))
print(searchInsert(nums = [1,3,5,6], target = 7))
print(searchInsert(nums = [1,3,5,6], target = 0))
print(searchInsert(nums = [1], target = 0))
    