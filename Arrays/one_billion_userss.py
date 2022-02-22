# We have N different apps with different user growth rates. At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), where g is the growth rate for that app. These apps will all be launched at the same time and no user ever uses more than one of the apps. We want to know how many total users there are when you add together the number of users from each app.
# After how many full days will we have 1 billion total users across the N apps?

# Signature
# int getBillionUsersDay(float[] growthRates)
# Input
# 1.0 < growthRate < 2.0 for all growth rates
# 1 <= N <= 1,000
# Output
# Return the number of full days it will take before we have a total of 1 billion users across all N apps.

# Example 1
# growthRates = [1.5]
# output = 52
# Example 2
# growthRates = [1.1, 1.2, 1.3]
# output = 79
# Example 3
# growthRates = [1.01, 1.02]
# output = 1047

import math

def getBillionUsersDay(growthRates):
  # Write your code here
  target = 10 ** 9
  
  left = math.floor(math.log(target, max(growthRates)))
  right =  math.ceil(math.log(target, min(growthRates)))

  print(left, right)

  while left < right:
    mid = (left + right) // 2
    users = 0
    for i in growthRates:
      users += (i ** mid)
    
    if users == target:
      return mid
    
    if users < target:
      left = mid + 1
    else:
      right = mid
  
  return left

print(getBillionUsersDay([1.5]))
print(getBillionUsersDay([1.1, 1.2, 1.3]))