# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:

# Input: arr = [100]
# Output: 1

# https://www.youtube.com/watch?v=_T-uynpWv78&ab_channel=TimothyHChang
class Solution:
    def maxTurbulenceSize(self, s: List[int]) -> int:
        l = 0
        r = 0
        n = len(s)
        output = 0
        
        if n ==1:
          return 1
        
        while r < n-1:
          while r < n-1 and (s[r-1] < s[r] > s[r+1] or  s[r-1] > s[r] < s[r+1]):
            r += 1
          while l < r and s[l] == s[l+1]:
            l += 1
          output = max(output, r-l+1)
          
          l = r
          r += 1
        
        return output