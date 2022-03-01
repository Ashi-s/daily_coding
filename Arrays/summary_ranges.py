# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

def summaryRanges(nums):
  if len(nums) == 0: return nums
  elif len(nums) == 1: return [str(nums[0])]
  n = len(nums)
  start = 0
  end = 1
  res = []
  count = 0
  while end < n:
    if nums[end] == nums[end-1] + 1:
      count += 1
      end += 1
    else:
      if count > 0:
        res.append(str(nums[start]) + '->' + str(nums[end-1]))
        start = end
        end = start+1
        count = 0
      else:
        res.append(str(nums[start]))
        start += 1
        end = start + 1
        count = 0
  
  if count > 0:
    res.append(str(nums[start]) + '->' + str(nums[end-1]))
  else:
    res.append(str(nums[start]))
  
  
  return res

nums = [0,2,4,5,7,8]
print(summaryRanges(nums))