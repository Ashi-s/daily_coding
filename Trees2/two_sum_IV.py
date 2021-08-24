# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
# Example 3:

# Input: root = [2,1,3], k = 4
# Output: true
# Example 4:

# Input: root = [2,1,3], k = 1
# Output: false
# Example 5:

# Input: root = [2,1,3], k = 3
# Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
      if not root:
        return False
      d = set()
      
      q = queue.Queue()
      q.put(root)
      while not q.empty():
        node = q.get()
        if k - node.val in d:
          return True
        else:
          d.add(node.val)
        if node.left:
          q.put(node.left)
        if node.right:
          q.put(node.right)
      return False