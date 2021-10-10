# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

import math
def countPrimes(n):
  prime = [1] * n
  prime[0] = prime[1] = 0

  for i in range(2, int(math.sqrt(n) + 1)):
    if prime[i]:
      for j in range(i*i, n, i):
        prime[j] = 0
  return sum(prime)

print(countPrimes(10))