# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# Example 1:


# Input: n = 3
# Output: 5
# Example 2:

# Input: n = 1
# Output: 1

# https://www.youtube.com/watch?v=Ox0TenN3Zpg

class Solution:
    def numTrees(self, n: int) -> int:
      numTree = [1] * (n+1)
      
      for node in range(2, n+1):
        total = 0
        for root in range(1, node+1):
          left = root - 1
          right = node - root
          total += numTree[left] * numTree[right]
        numTree[node] = total
      return numTree[n]
        