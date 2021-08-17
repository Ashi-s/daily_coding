# https://www.youtube.com/watch?v=IShCyNmsoL8&ab_channel=NideeshTerapalli
# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.


# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

def arithmetic_slices(nums):
  if len(nums) < 2:
        return 0
  dp = 0
  res = 0
  for i in range(2, len(nums)):
    if (nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]):
      dp += 1
      res += dp
    else:
      dp = 0
  return res

print(arithmetic_slices([1,2,3,4]))