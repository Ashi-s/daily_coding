# Given an array of n distinct elements, find the minimum number of swaps required to sort the array.

# Examples: 

# Input: {4, 3, 2, 1}
# Output: 2
# Explanation: Swap index 0 with 3 and 1 with 2 to 
#               form the sorted array {1, 2, 3, 4}.

# Input: {1, 5, 4, 3, 2}
# Output: 2

def minimum_swaps(arr):
  tmp = sorted(arr)

  d = {}
  count = 0
  for i in range(len(arr)):
    d[arr[i]] = i
  
  for i in range(len(arr)):
    init = arr[i]
    if arr[i] != tmp[i]:
      count += 1
      idx = d[tmp[i]]
      arr[i], arr[idx] = arr[idx], arr[i]

      d[arr[i]] = i
      d[init] = idx

  return count
arr = [101, 758, 315, 730, 472, 619, 460, 479]
print(minimum_swaps(arr))