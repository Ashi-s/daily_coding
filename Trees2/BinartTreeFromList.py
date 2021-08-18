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

def binary_tree_from_list(l):
  if not l:
    return "empty tree"
  
  root = BinaryTree(l[0])
  q = queue.Queue()
  q.put(root)
  i = 0

  while not q.empty():
    print('q: ', q)
    current =  q.get()
    if current.left is None and i < len(l):
      current.left = BinaryTree(l[i])
      i += 1
      q.put(current.left)
    
    if current.right is None and i < len(l):
      current.right = BinaryTree(l[i])
      i += 1
      q.put(current.right)
  return root.pre_order()

print(binary_tree_from_list([1,2,3,4,5,6]))


  
  