# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.

# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.


def canReach(arr, start):
    output = False
    memo = [i for i in arr]
    def helper(idx, memo):
      nonlocal output
      if memo[idx] == -1:#loop
        return
      if arr[idx] == 0:
        output = True
        return
      memo[idx] = -1 #visited
      lst = [idx+arr[idx], idx-arr[idx]]

      for i in lst:
        if i>=0 and i < len(arr):
          helper(i, memo)

    helper(start, memo)
    return output

print(canReach(arr =[1,1,1,1,1,1,1,1,0], start = 3))
            
        