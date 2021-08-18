import queue
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def pre_order(self):
    print(self.value)
    if self.left:
      self.left.pre_order()
    if self.right:
      self.right.pre_order()

def tree(l, i=None, root=None):
  if not l:
    return "empty list"
  if root is None:
    root = BinaryTree(l[0])
  if len(l) == 1:
    return root.value
  if i is None:
    i = 1
  
  while i < len(l):
    current = root
    if l[i] < current.value and i < len(l):
      if current.left is None:
        current.left = BinaryTree(l[i])
        i += 1
      else:
        tree(l, i, current.left)
        break
    
    if l[i] >= current.value and i < len(l):
      if current.right is None:
        current.right = BinaryTree(l[i])
        i += 1
      else:   
        tree(l, i, current.right)
        break
  return root.pre_order()

print(tree([23, 45, 12 ,3,5, 90, 44, 12, 5], None, None))

