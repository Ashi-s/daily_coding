# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

 

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]
def sortArrayByParityII(nums):
  for i in range(len(nums)):
    print(nums)
    if (i % 2 == 0 and nums[i] % 2 == 0) or (i % 2 != 0 and nums[i] % 2 != 0):
      continue
    else:
      j = i + 1
      # even = 1, odd = -1
      type = 'even' if nums[i] % 2 == 0 else 'odd'
      while j  < len(nums):
        if (type == 'even' and nums[j] % 2 != 0) or (type == 'odd' and nums[j] % 2 == 0):
          nums[i], nums[j] = nums[j], nums[i]
          break
        j += 1
  return nums

print(sortArrayByParityII([4,2,5,7]))