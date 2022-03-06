# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Example 1:


# Input: root = [2,1,3]
# Output: 1
# Example 2:


# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root):
      level = 0
      val = 0
      def helper(node, l):
        nonlocal level, val
        
        if not node: return
        
        if node.left:
          if l+1 > level:
            level = l+1
            val = node.left.val
          helper(node.left, l+1)
        
        if node.right:
          if l+1 > level:
            level = l+1
            val = node.right.val
          helper(node.right, l+1)
      
      if root and not root.left and not root.right:
        return root.val
      helper(root, 0)
      return val