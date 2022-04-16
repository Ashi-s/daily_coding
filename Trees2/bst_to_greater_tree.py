# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

# As a reminder, a binary search tree is a tree that satisfies these constraints:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# Example 2:

# Input: root = [0,null,1]
# Output: [1,null,1]
 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root):
    tmp = 0
    def helper(root):
      nonlocal tmp

      if root.right: helper(root.right)
      root.val, tmp = root.val + tmp, tmp + root.val
      if root.left: helper(root.left)
    
    return helper(root)

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)

a = root.left
b = root.right

a.left = TreeNode(0)
a.right = TreeNode(2)

b.left = TreeNode(5)
b.right = TreeNode(7)

c = a.right
d = b.right

c.right = TreeNode(3)
d.right = TreeNode(8)
# Input:
#         4
#     /      \
#    1        6
#  /    \    /  \
# 0      2   5   7
#         \       \
#         3        8
print(convertBST(root))

def traverse(root):
  if root.left:
    traverse(root.left)
  print(root.val, end=" ")

  if root.right:
    traverse(root.right)

print(traverse(root))