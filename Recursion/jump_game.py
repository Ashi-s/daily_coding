def canJump(nums):
        
  def helper(idx, N, res):
    if idx == N-1:
      res.append(True)
      return
    if idx >= N:
      return
    for i in range(1, nums[idx]+1):
      helper(idx+i, N, res)
    
  N = len(nums)
  res = []
  helper(0, N, res)
  print(res)
  return True if True in res else False

nums = [2,3,1,1,4]
print(canJump(nums))
nums1 = [3,2,1,0,4]
print(canJump(nums1))
nums2 = [3, 1, 0, 1, 1]
print(canJump(nums2))