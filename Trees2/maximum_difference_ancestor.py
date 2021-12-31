# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.


# Example 1:


# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
# Example 2:


# Input: root = [1,null,2,null,0,3]
# Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        _max = float('-inf')
        
        def helper(root):
          nonlocal _max
          if not root: return
          
          if root.left:
            tmp = abs(root.val - root.left.val)
            if tmp > _max: _max = tmp
            print('case 1: ', tmp, _max)
          
          if root.right:
            tmp = abs(root.val - root.right.val)
            if tmp > _max: _max = tmp
            print('case 2: ', tmp, _max)
          
          if root.left and root.left.left:
            tmp = abs(root.val - root.left.left.val)
            if tmp > _max: _max = tmp
            print('case 3: ', tmp, _max)
          if root.left and root.left.right:
            tmp = abs(root.val - root.left.right.val)
            if tmp > _max: _max = tmp
            print('case 4: ', tmp, _max)
          if root.right and root.right.left:
            tmp = abs(root.val - root.right.left.val)
            if tmp > _max: _max = tmp
            print('case 5: ', tmp, _max)
          if root.right and root.right.right:
            tmp = abs(root.val - root.right.right.val)
            if tmp > _max: _max = tmp
            print('case 6: ', tmp, _max)
          helper(root.left)
          helper(root.right)
          
        helper(root)
        return _max
          