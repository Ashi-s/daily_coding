def countQuadruplets( nums):
  count = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      for k in range(j+1, len(nums)):
        for x in nums[k+1:]:
          if x == (nums[i]+nums[j]+nums[k]):
            count += 1
  return count

print(countQuadruplets([9,6,8,23,39,23]))