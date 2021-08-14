# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Input: nums = [], target = 0
# Output: [-1,-1]
def firstAndLastElementSortedArray(nums, target):
  for idx, value in enumerate(nums):
    if value == target:
      iterator = idx + 1
      while True:
        if iterator < len(nums) and nums[iterator] == target:
          iterator += 1
        else:
          return [idx, iterator-1]
    else:
      continue
  return [-1, -1]

if __name__ == '__main__':
  nums = [5,7,7,8,8,10]
  target = 8
  nums1 = []
  target1 = 0
  print(firstAndLastElementSortedArray(nums, target))
  print(firstAndLastElementSortedArray(nums1, target1))