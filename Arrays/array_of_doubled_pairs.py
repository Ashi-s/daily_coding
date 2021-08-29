# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
# Example 1:

# Input: arr = [3,1,3,6]
# Output: false
# Example 2:

# Input: arr = [2,1,2,6]
# Output: false
# Example 3:

# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
# Example 4:

# Input: arr = [1,2,4,16,8,4]
# Output: false
import collections
def canReorderDoubled(arr):
  counter = collections.Counter(arr)
  print(counter)
  # counter = {}
  # for i in arr:
  #   if i in counter:
  #     counter[i] += 1
  #   else:
  #     counter[i] = 1
  
  for each in sorted(arr, key=abs):
    # if not counter.get(2*each): return False
    if counter.get(each) == 0: continue
    if counter.get(2*each) == 0: return False
    counter[each] -= 1
    counter[2*each] -= 1
  
  return True

print(canReorderDoubled([3,1,3,6]))
print(canReorderDoubled([4,-2,2,-4]))
print(canReorderDoubled([-4,-2,-2,-4]))