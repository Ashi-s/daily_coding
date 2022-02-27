# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), 
# where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

 

# Example 1:


# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:


# Input: root = [1,3,null,5,3]
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:


# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def widthOfBinaryTree(root) :
  q = deque()
  q.append((1,root))
  maxx = float('-inf')
  while q:
    size = len(q)
    maxx = max(maxx, q[-1][0] - q[0][0] +1)
    
    while size > 0:
      n, node = q.popleft()
      if node.left:
        q.append((2*n, node.left))
      if node.right:
        q.append((2*n+1, node.right))
      
      size -= 1
  
  return maxx
    