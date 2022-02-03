# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      dummy = res = ListNode()
      carry = 0
      while l1 or l2 or carry:
        if l1:
          val1 = l1.val
          l1 = l1.next
        else:
          val1 = 0
          
        if l2:
          val2 = l2.val
          l2 = l2.next
        else:
          val2 = 0
        
        total = (val1 + val2 + carry)
        num = total % 10
        carry = total // 10
        
        res.next = ListNode(num)
        res = res.next
      return dummy.next
        
          
        
      