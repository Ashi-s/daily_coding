
def getMaxLen(nums):
  
  def helper(idx, prod, count, res):
    if idx == N:
      return count
    res.append(nums[idx])
    prod *= nums[idx]
    if prod > 0:
      count = max(count, len(res))
    return helper(idx+1, prod, count, res)
    
  
  N = len(nums)
  output = 0
  for i in range(N):
    prod = 1
    res = []
    count = 0
    tmp = helper(i, prod, count, res)
    output = max(output,tmp)
  return output

print(getMaxLen([1,-2,-3,4]))
print(getMaxLen([0,1,-2,-3,-4]))

print(getMaxLen([-1,-2,-3,0,1]))
print(getMaxLen([-1,2]))
print(getMaxLen([1,2,3,5,-6,4,0,10]))

