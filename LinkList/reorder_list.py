# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Example 1:


# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:


# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
          return
        
        slow = head
        fast = head.next
        
        while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next
        
        slow = slow.next
        if fast.next:
          fast = fast.next
          
        
        #step 1 reverse pointer of seconf half
        
        prev = slow
        curr = slow.next
        prev.next = None
        
        while curr:
          tmp = curr.next
          curr.next = prev
          prev = curr
          curr = tmp
        
        # step 2 zig zag path
        trav = head
        while fast.next:
          tmp1 = trav.next
          tmp2 = fast.next
          trav.next = fast
          fast.next = tmp1
          trav = tmp1
          fast = tmp2
        