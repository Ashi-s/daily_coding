# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:

#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).



class BinaryTree:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
  def in_order(self):
    if self.left:
      self.left.in_order()
    print(self.val)
    if self.right:
      self.right.in_order()



def helper(l, op, r):
  
  if op == '+':
    return int(l) + int(r)
  if op == '-':
    return int(l) - int(r)
  if op == '*':
    return int(l) * int(r)
  if op == '/':
    return int(l) / int(r)
  

def evaluate(root):
  if not root:
    return None
  
  if root.val not in {'+', '-', '*', '/'}:
    return root.val
  
  else:
    return helper(evaluate(root.left), root.val, evaluate(root.right))

root = BinaryTree('*')
root.left = BinaryTree('+')
root.right = BinaryTree('+')

a_node = root.left
b_node = root.right

a_node.left = BinaryTree('3')
a_node.right = BinaryTree('2')
b_node.left = BinaryTree('4')
b_node.right = BinaryTree('5')

print(root.in_order())
print(evaluate(root))
