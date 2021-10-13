# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      summ = 0
      res = 0
      d = {0:1}
      
      for n in nums:
        summ += n
        diff = summ - k
        
        if diff in d:
          res += d[diff]
        if summ in d:
          d[summ] += 1
        else:
          d[summ] = 1
          
      return res