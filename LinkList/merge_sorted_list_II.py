# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
      def merge2(l1, l2):
        head = curr = ListNode(0)
        
        while l1 and l2:
          if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
          else:
            curr.next = l2
            l2 = l2.next
          curr = curr.next
        curr.next = l1 or l2
        
        return head.next
        
      interval = 1
      
      while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
          lists[i] = merge2(lists[i], lists[i+interval])
        interval *= 2
      
      return lists[0] if len(lists) > 0 else None
        
        
        
      