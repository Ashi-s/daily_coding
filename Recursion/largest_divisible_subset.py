# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.
# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
      nums.sort()
      n = len(nums)
      
      dp = [[num] for num in nums]
      
      for i in range(n-1):
        for j in range(i+1, n):
          if nums[j] % nums[i] == 0 and len(dp[i]) >= len(dp[j]):
            dp[j] = dp[i] + [nums[j]]
            
      dp.sort(key=len)
      return dp[-1]
        