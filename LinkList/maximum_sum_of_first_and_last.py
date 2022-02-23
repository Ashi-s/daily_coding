# Given a singly linked list where each element contains a number and a pointer to the head of the list. 
# Sum the first and last data and remove these nodes. Then sum the first and last data of the resulting linked list and remove these two nodes.
# Keep doing this till the list becomes empty. we have to find the maximum sum obtained from the resulting sum in O(1) space complexity.
# The list is a singly linked list with even nodes.

class LL:
  def __init__(self, val):
    self.data = val
    self.next = None

def reverse(head, dummy):
    prev = None
    current = head
    while current:
        next_ptr = current.next
        current.next = prev
        prev = current
        current = next_ptr
    
    dummy.next = prev
    
def maximumPages(head):
    # Write your code here
    tail = tail2 = head
    length = 0
    while tail:
        length += 1
        tail = tail.next

    length = (length // 2) - 1
    
    while length > 0:
        tail2 = tail2.next
        length -= 1
    
    reverse(tail2.next, tail2)
    tail3 = tail2.next
    maxx = float('-inf')
    while tail3:
        maxx = max(maxx, head.data + tail3.data)
        head = head.next
        tail3 = tail3.next
    
    return maxx


l = LL(1)
l.next = LL(4)
l.next.next = LL(3)
l.next.next.next = LL(2)
l.next.next.next.next = LL(7)
l.next.next.next.next.next = LL(8)

print(maximumPages(l))