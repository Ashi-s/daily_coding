# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tor, hare = nums[0], nums[0]
        
        while True:
          tor = nums[tor]
          hare = nums[nums[hare]]
          
          if tor == hare:
            break
        
        tor = nums[0]
        while tor != hare:
          tor = nums[tor]
          hare = nums[hare]
        
        return hare