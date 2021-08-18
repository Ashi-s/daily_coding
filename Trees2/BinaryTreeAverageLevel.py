'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
/   /  \
5   15   7
Output: [3, 14.5, 9]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
'''

import queue
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def average(root):
  q = queue.Queue()
  q.put(root)
  out = []
  while not q.empty():
    total = 0
    n=N= q.qsize()
    while n > 0:
      node = q.get()
      total += node.value
      if node.left:
        q.put(node.left)
      if node.right:
        q.put(node.right)
      n -= 1
    out.append(total/N)
  return out

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)

node2 = root.left
node3 = root.right

node2.left = BinaryTree(5)
node3.left = BinaryTree(15)
node3.right = BinaryTree(7)

print(average(root))

