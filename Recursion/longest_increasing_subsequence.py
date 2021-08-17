# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# https://www.youtube.com/watch?v=cjWnW0hdF1Y&ab_channel=NeetCode

def lengthOfLIS(nums):
    LIS = [1]*len(nums)
    
    for i in range(len(nums)-1, -1, -1):
      for j in range(i+1, len(nums)):
        if nums[i] < nums[j]:
          LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))