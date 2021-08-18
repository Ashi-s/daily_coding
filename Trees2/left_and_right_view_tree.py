'''
            1
        2       3
    4               5
                6
output: LeftView: 1,2,4,6
        RightView: 1,3,5,6
'''
import queue

class Tree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  def preOrder(self):
    print(self.value)
    if self.left:
      self.left.preOrder()
    if self.right:
      self.right.preOrder()

  
def left_view(root):
  q = queue.Queue()
  q.put(root)
  out = []

  while not q.empty():
    n = q.qsize()
    left = n

    while n > 0:
      node = q.get()

      if n == left:
        out.append(node.value)
      if node.left:
        q.put(node.left)
      if node.right:
        q.put(node.right)
      n -= 1
  return out

def right_view(root):
  q = queue.Queue()
  out = []
  q.put(root)

  while not q.empty():
    n = q.qsize()
    while n > 0:
      node = q.get()
      if n == 1:
        out.append(node.value)
      if node.left:
        q.put(node.left)
      if node.right:
        q.put(node.right)
      n -= 1
  return out


root= Tree(1)
root.left = Tree(2)
root.right = Tree(3)

a_node =root.left
b_node = root.right

a_node.left = Tree(4)
b_node.right = Tree(5)

c_node = b_node.right
c_node.left = Tree(6)

print(root.preOrder())
print('Left View: ', left_view(root))
print('Right View: ',right_view(root))
