import queue

class BinaryTree:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

  def insert_left(self, val):
    if self.left is None:
      self.left = BinaryTree(val)
    else:
      current = BinaryTree(val)
      current.left = self.left
      self.left = current

  def insert_right(self, val):
    if self.right is None:
      self.right = BinaryTree(val)
    else:
      current = BinaryTree(val)
      current.right = self.right
      self.right = current

  def pre_order(self):
    print(self.value)
    if self.left:
      self.left.pre_order()
    if self.right:
      self.right.pre_order()

  def in_order(self):
    if self.left:
      self.left.in_order()
    print(self.value)
    if self.right:
      self.right.in_order()

  def post_order(self):
    if self.left:
      self.left.post_order()
    if self.right:
      self.right.post_order()
    print(self.value)

  def BFS(self):
    q = queue.Queue()
    q.put(self)

    while not q.empty():
      current = q.get()
      print(current.value)

      if current.left:
        q.put(current.left)
      if current.right:
        q.put(current.right)


    

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left
b_node.insert_right('d')

c_node = a_node.right
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right
e_node = c_node.left
f_node = c_node.right

print('pre-order: ',a_node.pre_order())
print('in-order: ', a_node.in_order())
print('post-order: ', a_node.post_order())

###BFS
print('BFS: {0}'.format(a_node.BFS()))

