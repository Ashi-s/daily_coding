# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

def findDuplicates(nums):
  res = []
  
  for i in range(len(nums)):
    idx = abs(nums[i]) - 1
    if nums[idx] < 0:
      res.append(idx+1)
    nums[idx] = -nums[idx]
  
  return res

# print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([2,2]))
# print(findDuplicates([4,3,2,7,8,2,3,1]))

