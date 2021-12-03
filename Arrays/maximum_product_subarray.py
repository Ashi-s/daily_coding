# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# It is guaranteed that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return nums[0]
      
      max_so_far, min_so_far, global_max = nums[0], nums[0], nums[0]
      
      for i in range(1, len(nums)):
        max_so_far, min_so_far = max(max_so_far*nums[i], min_so_far*nums[i], nums[i]), min(max_so_far*nums[i], min_so_far*nums[i], nums[i])
        global_max = max(global_max, max_so_far)
        
      return global_max