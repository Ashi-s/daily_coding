# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, 
# and every node has no left child and only one right child.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:


# Input: root = [5,1,7]
# Output: [1,null,5,null,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse(root):
  if root.left:
    traverse(root.left)
  print(root.val, end=" ")

  if root.right:
    traverse(root.right)

def increasingBST(root):
  def inOrder(root):
    nonlocal dummy
    if root.left:
      inOrder(root.left)
    
    dummy.right = TreeNode(root.val)
    # print(dummy.right.val)
    dummy = dummy.right
    
    if root.right:
      inOrder(root.right)
  
  curr = dummy = TreeNode(0)
  inOrder(root)
  return traverse(curr.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)

a = root.left
b = root.right

a.left = TreeNode(2)
a.right = TreeNode(4)

b.right = TreeNode(8)

c = a.left
d = b.right

c.left = TreeNode(1)

d.left = TreeNode(7)
d.right = TreeNode(9)
# Input:
#         5
#      /      \
#     3        6
#   /    \      \
#  2      4      8
# /             /  \
# 1            7    9


print(increasingBST(root))