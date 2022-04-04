# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      # one traversal
      ptr1 = ptr2 = curr = head
      
      for _ in range(k-1):
        curr = curr.next
      ptr1 = curr
      
      while curr.next:
        curr = curr.next
        ptr2 = ptr2.next
      
      ptr1.val, ptr2.val = ptr2.val, ptr1.val
      
      return head
        
      
      
      
      
#Two time traversal
#         ptr1 = ptr2 = curr = head
        
#         l = 0
#         while curr:
#           if l == k-1:
#             ptr1 = curr
          
#           l += 1
#           curr = curr.next
        
#         tmp = l - k
#         curr = head
#         while tmp > 0:
#           curr = curr.next
#           tmp -= 1
#         ptr2 = curr
#         ptr1.val, ptr2.val = ptr2.val, ptr1.val
        
#         return head
        