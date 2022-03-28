# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

 

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
          mid = (left+right) // 2
          
          if nums[mid] == target:
            return True
          
          while left<mid and nums[left]==nums[mid]:
            left+=1
          #left sorted
          if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
              left = mid+1
            else:
              right = mid-1
          else:
            if target > nums[right] or target < nums[mid]:
              right = mid-1
            else:
              left = mid+1
        
        return False