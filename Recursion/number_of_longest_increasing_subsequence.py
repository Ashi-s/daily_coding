# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

# Input: nums = [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

# https://www.youtube.com/watch?v=WcQ_y9TWhhw&ab_channel=KnowledgeCenter


def findNumberOfLIS(nums):
    LIS = [1] * len(nums)
    count = [1] * len(nums)
    
    for i in range(len(nums)-1, -1, -1):
      for j in range(i+1, len(nums)):
        if nums[i] < nums[j]:
          LIS[i] = max(LIS[i], 1+LIS[j])
      if i+1 < len(nums) and LIS[i] == LIS[i+1]:
        count[i] = count[i+1]+  1
    return max(count)

# print(findNumberOfLIS([2,2,2,2,2]))

#why count[i] = max(count)+  1?
print(findNumberOfLIS([1,2,4,3,5,4,7,2]))