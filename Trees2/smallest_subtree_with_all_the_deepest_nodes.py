# Given the root of a binary tree, the depth of each node is the shortest distance to the root.

# Return the smallest subtree such that it contains all the deepest nodes in the original tree.

# A node is called the deepest if it has the largest depth possible among any node in the entire tree.

# The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

# Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
      
      def depth(root):
        if root is None:
          return 0
        else:
          return 1 + max(depth(root.left), depth(root.right))
      
      self.ans = None
      def helper(root):
        if root is None:
          return
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        
        if l_depth == r_depth:
          self.ans = root
          return
        
        if l_depth > r_depth:
          helper(root.left)
        
        if l_depth < r_depth:
          helper(root.right)
          
      helper(root)
      return self.ans
        