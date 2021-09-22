# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      
      prev = nums[0]
      count = 0
      _max = 0
      for i in range(len(nums)):
        if nums[i] == 1 and prev == 1:
          count += 1
        elif nums[i] == 1:
          _max = max(_max, count)
          count = 1
        else:
          _max = max(_max, count)
          count = 0
        prev = nums[i]
      
      _max = max(_max, count)
      return _max