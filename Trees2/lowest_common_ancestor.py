# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:


# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if root.val == p.val or root.val == q.val:
          return root
        deq = deque()
        deq.append(root)
        
        parent = {}
        
        while not (p in parent and q in parent):
          node = deq.popleft()
          if node.left:
            parent[node.left] = node
            deq.append(node.left)
          
          if node.right:
            parent[node.right] = node
            deq.append(node.right)
        
        common = set()
        
        trav = p
        
        while trav in parent:
          common.add(trav)
          trav = parent[trav]
        
        common.add(root)
        
        trav = q
        while not trav in common:
          trav = parent[trav]
        
        return trav
     