# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      if sum(nums) % 2 != 0:
        return False
      dp = set()
      dp.add(0)
      target = sum(nums) // 2
      
      for i in nums:
        next_dp = dp.copy()
        for each in dp:
          if i+each == target:
            return True
          next_dp.add(each + i)
        dp = next_dp
      return False