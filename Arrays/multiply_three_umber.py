# This problem was asked by Facebook.

# Given a list of integers, return the largest product that can be made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

# You can assume the list has at least three integers.

def multiply_three(nums):
  nums.sort()

  return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(multiply_three([-1, -2, -3]))
print(multiply_three([-10, -10, 5, 2]))
