# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# // https://www.youtube.com/watch?v=tl27epAepI8&ab_channel=abrar

# // input : [2,3,4] ->> 6
# // input : [1,20,3] ->> 20
# // input : [5, 1, 1, 6] ->> 11
# // max sum and cannot pick adjacent together

#time O(n) - space O(n)
def max_sum(nums):
  if len(nums) == 0:
    return 0
  n = len(nums)
  pick = [0] * n
  dont_pick = [0] * n
  pick[0] = nums[0]
  for i in range(1, n):
    pick[i] = dont_pick[i-1] + nums[i]
    dont_pick[i] = max(pick[i-1], dont_pick[i-1])

  return max(pick[-1], dont_pick[-1])

# time O(n) - space O(1)
def max_sum1(nums):
  if len(nums) == 0:
    return 0
  n = len(nums)
  pick = nums[0]
  dont_pick = 0

  for i in range(1, n):
    pick, dont_pick = dont_pick + nums[i], max(pick, dont_pick)

  return max(pick, dont_pick)
    
print(max_sum([2,3,4]))
print(max_sum([1,20,3]))
print(max_sum([5,1,1,6]))

print(max_sum1([2,3,4]))
print(max_sum1([1,20,3]))
print(max_sum1([5,1,1,6]))
