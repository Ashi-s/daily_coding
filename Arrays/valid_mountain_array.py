# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
      if len(arr) <= 2:
        return False
      
      is_decreasing = False
      has_increased = False
      for i in range(1, len(arr)):
        if not is_decreasing:
          if arr[i] > arr[i-1]:
            has_increased = True
            continue
          elif arr[i] == arr[i-1]:
            return False
          else:
            is_decreasing = True
        else:
          if arr[i] < arr[i-1]:
            continue
          else:
            return False
      
      return has_increased and is_decreasing