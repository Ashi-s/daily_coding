# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

def jump(nums):
# M1 Recursion
#       n = len(nums)
#       def helper(idx, curr):
#         nonlocal res
#         if idx == n-1:
#           res = min(res, curr)
#           return
#         if idx >= n:
#           return
#         for i in range(1, nums[idx]+1):
#           helper(idx+i, curr+1)
      
      
#       res = float('inf')
#       helper(0, 0)
#       return res
    n = len(nums)
    dp = [float('inf') for _ in range(n)]
    dp[0] = 0
    for i in range(n-1):
        far = min(i+nums[i], n-1)
        for j in range(i+1, far+1):
            dp[j] = min(dp[j], 1 + dp[i])
    # print(dp)
    return dp[-1] if dp[-1] != float('inf') else -1 