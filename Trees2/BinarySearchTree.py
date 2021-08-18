import queue
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  #search
  def search(self, value):
    if self.left and value < self.value:
      return self.left.search(value)
    elif self.right and value > self.value:
      return self.right.search(value)

    return value == self.value

  #insert
  def insert(self, value):
    if self.left and value < self.value:
      self.left.insert(value)
    elif value < self.value:
      self.left = BinarySearchTree(value)
    elif self.right and value > self.value:
      self.right.insert(value)
    elif value > self.value:
      self.right = BinarySearchTree(value)

  #traverse DFS/preOrder
  def dfs(self):
    print(self.value)
    if self.left:
      self.left.dfs()
    if self.right:
      self.right.dfs()

  # traverse BFS
  def bfs(self):
    q = queue.Queue()
    root = self
    q.put(root)

    while not q.empty():
      node = q.get()
      print(node.value)
      if node.left:
        q.put(node.left)
      if node.right:
        q.put(node.right) 
  
  #delete
  def delete(self, value, parent=None):
    #traverse to find the node
    if self.left and value < self.value:
      return self.left.delete(value, self)
    elif value <self.value:
      return False
    elif self.right and value > self.right:
      return self.right.delete(value, self)
    elif value > self.right:
      return False
    else:
      #delete case 1
      if self.left is None and self.right is None and self == parent.left:
        parent.left = None
        self.clear_node()
      #delete case 2
      elif self.left is Noen and self.right is None and self == parent.right:
        parent.right = None
        self.clear_node()
      #case 3
      elif self.left and self.right is None and self == parent.left:
        parent.left = self.left
        self.clear_node()
      #case 4
      elif self.right and self.left is None and self == parent.right:
        parent.right = self.right
        self.clear_node()
      #case 5
      elif self.left and self.right is None and self == parent.right:
        parent.right = self.left
        self.clear_node()
      #case 6
      elif self.right and self.left is None and self == parent.left:
        parent.left = self.right
        self.clear_node()
      #case 7
      else:
        self.value = self.right.min_value()
        self.right.delete(self.value, self)
  

  def clear_node(self):
    self.value = None
    self.left = None
    self.right = None
  
  def min_value(self):
    if self.left:
      return self.left.min_value()
    return self.value
  