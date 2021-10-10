# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

#M1 O(nlogn) bcoz of the sort
def longestConsecutive(nums):
  if len(nums) < 2:
    return len(nums)
  nums.sort()
  
  longest = 1
  current = 1
  
  for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
      if nums[i] == nums[i-1] + 1:
        current += 1
      else:
        longest = max(longest, current)
        current = 1
  
  return max(longest, current)

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))

#M2 O(n)
def longestConsecutive2(nums):
  nums = set(nums)
  longest = 0

  for n in nums:
    if n-1 not in nums:
      current_num = n
      current = 1
      while current_num + 1 in nums:
        current_num += 1
        current += 1

      longest = max(longest, current)


  return longest

nums1 = [100,4,200,1,3,2]
print(longestConsecutive2(nums1))
