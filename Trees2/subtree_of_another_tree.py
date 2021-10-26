# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:

# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same(self, root, subRoot):
      if not root and not subRoot:
        return True
      elif root and subRoot and root.val == subRoot.val:
        return self.is_same(root.left, subRoot.left) and self.is_same(root.right, subRoot.right)
      else:
        return False
        
      
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
          return True
        if not root:
          return False
        if self.is_same(root, subRoot):
          return True
        else:
          return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        