# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

#combination II each num in candidate can only be used once
# Input: candidates = [10,1,2,7,6,1,5], target = 8
def combination_sum(nums, target):
  result = []

  helper(result, nums, target, 0, [], 0)
  return result

def helper(result, nums, target, index, current, total):
  if total == target:
    result.append(current.copy())
    return
  
  if total > target or index >= len(nums):
    return

  current.append(nums[index])
  helper(result, nums, target, index+1, current, total + nums[index])

  current.pop()
  helper(result, nums, target, index+1, current, total)

# print(combination_sum([2,3,6,7], 7))
print(combination_sum([10,1,2,7,6,5], 8))