# This problem was asked by LinkedIn.

# Determine whether a tree is a valid binary search tree.

# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def valid_bst(root):
  if not root:
    return False

  helper(root)
  return True


def helper(root):
  if root.left:
    if root.left.val <= root.val:
      helper(root.left)
    else:
      return False

  if root.right:
    if root.right.val > root.val:
      helper(root.right)
    else:
      return False
  return
    
