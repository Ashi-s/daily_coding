# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def three_sum(nums):
  output = []
  nums.sort() #[-4,-1,-1, 0,1,2]
  for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]: continue
    left = i+1
    right = len(nums) - 1

    while left < right:
      total = nums [i] + nums[left] + nums[right]
      # 0
      if total == 0:
        output.append([nums [i] , nums[left] , nums[right]])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left+1]: left += 1
        while left < right and nums [right] == nums[right-1]: right -= 1
      # <
      elif total < 0:
        left += 1
      # >
      elif total > 0:
        right -= 1
  return output

if __name__ == '__main__':
  nums = [-1,0,1,2,-1,-4,-4,-4]
  print(three_sum(nums))

      
