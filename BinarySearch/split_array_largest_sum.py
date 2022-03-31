# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

# Write an algorithm to minimize the largest sum among these m subarrays.

 

# Example 1:

# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
# Example 3:

# Input: nums = [1,4,4], m = 3
# Output: 4

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #binary search [7,2,5,10,8]
        #min value possible would be 10 (take the maximum alone)
        #max value possibe would be sum of nums 32
        left, right = 0, 0
        for i in nums:
          if i > left:
            left = i
          right += i
        
        # our answer has be in between left and right
        
        while left < right:
          mid = (left + right) // 2
          
          if self.canSplit(mid, nums, m):
            right = mid
          else:
            left = mid+1
        
        return left
    
    def canSplit(self, summ, nums,  m):
      # no. of splits possible
      count = 1
      total = 0
      
      for i in nums:
        total += i
        
        # if total is greater than mid sum value
        # then we increase count and start a new subarray
        if total > summ:
          total = i
          count += 1
        
        # at any point number of splits is greater than m
        #return False
        if count > m:
          return False
      
      #return True if split is possible
      return True