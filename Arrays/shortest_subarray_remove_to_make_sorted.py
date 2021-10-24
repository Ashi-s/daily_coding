# https://www.youtube.com/watch?v=T3mVs4XHV1E

# Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

# A subarray is a contiguous subsequence of the array.

# Return the length of the shortest subarray to remove.

# Example 1:

# Input: arr = [1,2,3,10,4,2,3,5]
# Output: 3
# Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
# Another correct solution is to remove the subarray [3,10,4].
# Example 2:

# Input: arr = [5,4,3,2,1]
# Output: 4
# Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
# Example 3:

# Input: arr = [1,2,3]
# Output: 0
# Explanation: The array is already non-decreasing. We do not need to remove any elements.
# Example 4:

# Input: arr = [1]
# Output: 0

class Solution:
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    ans = 0
    n = len(arr)
    peak = 0
    valley = n-1
    
    while peak < n-1 and arr[peak] <= arr[peak + 1]:
      peak += 1
    
    if peak == n-1:
      return 0
    
    while valley > peak and arr[valley] >= arr[valley-1]:
      valley -= 1
      
    ans = min(n - peak - 1, valley)
    i = 0
    j= valley
    while i <= peak and j < n:
      if arr[j] >= arr[i]:
        ans = min(ans, j -i-1)
        i += 1
      else:
        j += 1
    return ans
        