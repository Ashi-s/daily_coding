# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getSize(head):
          count = 0
          node = head
          
          while True:
            count += 1
            # point tail to head
            if node.next is None:
              node.next = head
              break
            
            node = node.next
          
          return count
        
        if not head:
          return None
        
        size = getSize(head)
        
        k = k % size
        
        curr = head
        
        for _ in range(size-k-1):
          curr = curr.next
          
        new_head = curr.next
        curr.next = None
        
        return new_head