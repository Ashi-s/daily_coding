class Node:
  def __init__(self, val=0):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def traverse(self):
    node = self.head

    while node != None:
      print(node.val)
      node = node.next

    return
  
  def reverse(self):
    current = self.head
    nex = current.next

    if current is None:
      return []
    elif current.next == None:
      return current
    
    while nex.next != None:
      temp = nex.next
      nex.next = current
      current = nex
      nex = temp
    nex.next = current
    current.next = None


l = LinkedList()
l.head = Node(23)
n1 = Node(4)
n2 = Node(324)
n3 = Node(34)
n4 = Node(9)

l.head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

l.traverse()
l.reverse()
l.traverse()