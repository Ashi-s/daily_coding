
def firstMissingPositive(nums):
  N = len(nums)
  temp = [None] * N
  for x in nums:
    print(temp)
    if 1<=x<=N:
      temp[x-1] = x
  for i in range(N):
    if temp[i] == None:
      return i+1
  return N+1 
if __name__ == '__main__':
  nums = [7,8,9,11,12] #1
  nums1 = [1, 2, 3, 4, 5] #6
  nums2 = [1,2,0]
  print(firstMissingPositive(nums))
  print(firstMissingPositive(nums1))
  print(firstMissingPositive(nums2))