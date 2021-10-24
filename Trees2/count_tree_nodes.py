# Given the root of a complete binary tree, return the number of the nodes in the tree.

# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:

# Input: root = [1,2,3,4,5,6]
# Output: 6
# Example 2:

# Input: root = []
# Output: 0
# Example 3:

# Input: root = [1]
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
      
      def helper(root):
        if not root:
          return
        if root.left:
          self.ans += 1
          helper(root.left)
        if root.right:
          self.ans += 1
          helper(root.right)
      
      if not root:
        return 0
      self.ans = 1
      helper(root)
      return self.ans
      