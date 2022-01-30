# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

#M1 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
          nums.insert(0, nums.pop())
          k -= 1

# M2
# 1. reverse whole array, 2. reverse first K, 3. reverse K+1 to end
def rotate(nums, k):
  n = len(nums)
  k = k % n
  reverse(nums, 0, n-1)
  reverse(nums, 0, k-1)
  reverse(nums, k, n-1)
  return nums

def reverse(nums, start, end):
  while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1

nums = [1,2,3,4,5,6,7]
print(rotate(nums, 3))
