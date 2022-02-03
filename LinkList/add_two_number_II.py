# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:


# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      s1, s2 = 0, 0
      while l1:
        s1 *= 10
        s1 += l1.val
        l1 = l1.next
      while l2:
        s2 *= 10
        s2 += l2.val
        l2 = l2.next
      
      s3 = s1 + s2
      
      prev = None
      
      if s3 == 0:
        return ListNode(0)
      while s3 != 0:
        head = ListNode(s3 % 10)
        s3 //= 10
        head.next = prev
        prev = head
      
      return prev