# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

# As the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# Example 2:

# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

from collections import Counter
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        MOD = 10**9 + 7
        res = 0
        keys = sorted(count)
        
        for i, v in enumerate(keys):
          j = i
          k = len(keys)-1
          
          while j <= k:
            x, y, z = keys[i], keys[j], keys[k]
            tmp =  keys[i] + keys[j] + keys[k]
            if tmp > target:
              k -= 1
            elif tmp < target:
              j += 1
            else: #equal
              if i < j < k:
                res += count[x] * count[y] * count[z]
              elif i == j < k:
                res += count[x] * (count[x]-1)//2 * count[z]
              elif i < j == k:
                res += count[x] * count[y] * (count[y]-1)//2
              else:#i==j==k
                res += count[x] * (count[x]-1) * (count[x]-2) // 6
            
              j += 1
              k -= 1
          
        return res % MOD
           