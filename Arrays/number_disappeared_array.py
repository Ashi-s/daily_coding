# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      for i in range(len(nums)):
        tmp = abs(nums[i])
        if nums[tmp-1] > 0:
          nums[tmp-1] = -nums[tmp-1]
      res = []
      for i in range(len(nums)):
        if nums[i] > 0:
          res.append(i+1)
      return res
#       _set = set()
#       for i in range(1, len(nums)+1):
#         _set.add(i)
      
#       for i in nums:
#         if i in _set:
#           _set.remove(i)
          
#       return list(_set)
        