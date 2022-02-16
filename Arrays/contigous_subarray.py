def count_subarrays(nums):
  # Write your code here
  res = []
  for i in range(len(nums)):
    count = 1
    for j in range(i-1, -1, -1):
      if nums[i] > nums[j]:
        count += 1
      else: break
    for k in range(i+1, len(nums)):
      if nums[i] > nums[k]:
        count += 1
      else: break
    
    res.append(count)
  
  return res

arr = [3, 4, 1, 6, 2]
print(count_subarrays(arr))