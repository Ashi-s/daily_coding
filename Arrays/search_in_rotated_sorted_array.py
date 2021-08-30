# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      if len(nums) == 0:
        return -1
      
      i = len(nums) // 2
      j = len(nums) // 2 + 1
      
      for k in range(len(nums)//2 + 1):
        if nums[i] == target:
          return i
        elif j < len(nums) and nums[j] == target:
          return j
        
        i -= 1
        j += 1
      
      return -1