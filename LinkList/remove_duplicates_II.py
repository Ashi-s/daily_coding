# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#  Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        if not head:
          return None
        if head and not head.next:
          return head
        
        dummy = ListNode(-101)
        dummy.next = head
        curr = head
        prev = dummy
        
        while curr and curr.next:
          
          if curr.val == curr.next.val:
            tmp = curr
            while tmp and tmp.val == curr.val:
              tmp = tmp.next
            prev.next = tmp
            curr = prev.next
          else:
            curr = curr.next
            prev = prev.next
        
        return dummy.next