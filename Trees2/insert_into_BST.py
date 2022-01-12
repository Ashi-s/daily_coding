# You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
# Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      
      def helper(node, val):
        if not node.left and node.val > val:
          node.left = TreeNode(val)
          return
        if not node.right and node.val < val:
          node.right = TreeNode(val)
          return
        if node.left and node.val > val:
          helper(node.left, val)
        if node.right and node.val < val:
          helper(node.right, val)
      
      if not root:
        return TreeNode(val)
      helper(root, val)
      return root
        