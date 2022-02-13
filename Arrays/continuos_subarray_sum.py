# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

# An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

# Example 1:

# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
# Example 2:

# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
# Example 3:

# Input: nums = [23,2,6,4,7], k = 13
# Output: false

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      d = {0:-1}
      summ = 0
      for i in range(len(nums)):
        summ += nums[i]
        tmp = summ % k
        
        if tmp in d:
          if i - d[tmp] >= 2:
            return True
        else:
          d[tmp] = i
      return False

#M2 TLE
#       d = {nums[0]: 0}
      
#       for i in range(1, len(nums)):
        
#         for key in list(d.keys()):
#           if (key + nums[i]) % k == 0:
#             return True
#           else:
#             del d[key]
#             tmp = key + nums[i]
#             d[tmp] = 0
#         d[nums[i]] = 0
#       return False

# M1 Two loops TLE
#       for i in range(len(nums)):
#         tmp = nums[i]
#         for j in range(i+1, len(nums)):
#           tmp += nums[j]
#           if tmp % k == 0:
#             return True
      
#       return False