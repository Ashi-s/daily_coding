# Given the root of a binary tree, return the sum of all left leaves.

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
      
      def helper(root):
        if root.left and (not root.left.left and not root.left.right):
          res.append(root.left.val)
          
        if root.left:
          helper(root.left)
        if root.right:
          helper(root.right)
          
      if not root.left and not root.right:
        return 0
      res = []
      helper(root)
      return sum(res)
        