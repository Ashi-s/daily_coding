# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

def findMaxLength(nums):
  """
  :type nums: List[int]
  :rtype: int
  """
  dic = {0:-1}
  count = 0
  maxlen = 0
  for i in range(len(nums)):
      count += (1 if nums[i] == 1 else -1)
      if count not in dic:
          dic[count] = i
      else:
          maxlen = max(maxlen, i - dic[count])
  return maxlen

print(findMaxLength([0,1, 1,1,0,1,0,1]))