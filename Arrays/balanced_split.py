# Balanced Split
# Given an array of integers (which may include repeated integers), determine if there's a way to split the array into two subsequences A and B such that the sum of the integers in both arrays is the same, and all of the integers in A are strictly smaller than all of the integers in B.
# Note: Strictly smaller denotes that every integer in A must be less than, and not equal to, every integer in B.

# Signature
# bool balancedSplitExists(int[] arr)
# Input
# All integers in array are in the range [0, 1,000,000,000].
# Output
# Return true if such a split is possible, and false otherwise.

# Example 1
# arr = [1, 5, 7, 1]
# output = true
# We can split the array into A = [1, 1, 5] and B = [7].
# Example 2
# arr = [12, 7, 6, 7, 6]
# output = false
# We can't split the array into A = [6, 6, 7] and B = [7, 12] since this doesn't satisfy the requirement that all integers in A are smaller than all integers in B.

def balancedSplitExists(arr):
  # Write your code here
  summ = sum(arr)
  if summ % 2 != 0:
    return False
  arr.sort()
  target = summ // 2
  
  tmp = 0
  _set = set()
  for i in range(len(arr)):
    tmp += arr[i]
    _set.add(arr[i])
    if tmp == target:
      break
    elif tmp > target:
      return False
  
  for j in range(i+1, len(arr)):
    if arr[j] in _set:
      return False
  
  return True

arr_1 = [2, 1, 2, 5] #True
print(balancedSplitExists(arr_1))

arr_2 = [3, 6, 3, 4, 4] #False
print(balancedSplitExists(arr_2))