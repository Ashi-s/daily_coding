# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:


# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
# Example 2:


# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
# Example 3:

# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head) :
  ll = []
  curr = output = ListNode(0)
  node = head
  while node:
    ll.append(node.val)
    node = node.next
  
  ll.sort()
  
  
  for i in ll:
    output.next = ListNode(i)
    output = output.next
  
  return curr.next