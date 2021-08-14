# https://www.youtube.com/watch?v=ZI2z5pq0TqA&t=1378s&ab_channel=NeetCode
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


def trap_rain_water(nums):
  count = 0

  for i in range(len(nums)):
    if len(nums[i+1:]) > 0:
      max_right = max(nums[i+1:])
    else:
      max_right = 0
    
    if i-1 >= 0:
      if len(nums[:i]) > 0:
        max_left = max(nums[:i-1])
    else:
      max_left = 0
      

    water = min(max_right, max_left)
    print('let, right,water: ', max_left, max_right, water)

    if water - nums[i] > 0:
      count += water
  return count


#M-2 Neetcode
def trap_rain_water2(nums):
  max_left = nums[0]
  max_right = nums[len(nums)-1]
  count = 0

  left = 0
  right = len(nums) - 1

  while left < right:
    if max_left < max_right:
      left += 1
      max_left = max(max_left, nums[left])
      count += max_left - nums[left]
    else:
      right -= 1
      max_right = max(max_right, nums[right])
      count += max_right - nums[right]
  return count
print(trap_rain_water2([3,0,1,3,0,5]))