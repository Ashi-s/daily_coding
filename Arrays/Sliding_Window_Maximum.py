# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

def maxSlidingWindow(nums, k):
  # _max = float('-inf')
  res = []
  for i in range(len(nums)-k+1):
    # _max = max(nums[i:i+k])
    print(i, nums[i:i+k])
    res.append(max(nums[i:i+k]))
  return res
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3))