# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Example 1:

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#REFERENCE SOLUTION
# https://leetcode.com/problems/path-sum-iii/discuss/170367/Python-solution

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
      
      def helper(node, prev_sum, summ):
        if not node:
          return
        
        curr_sum = prev_sum + node.val
        
        if curr_sum - summ in rec:
          self.count += rec[curr_sum - summ]
          
        if curr_sum in rec:
          rec[curr_sum] += 1
        else:
          rec[curr_sum] = 1
          
        helper(node.left, curr_sum, summ)
        helper(node.right, curr_sum, summ)
        
        rec[curr_sum] -= 1
        
      self.count = 0
      rec = {0:1}
      helper(root, 0, targetSum)
      return self.count
        