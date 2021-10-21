# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:

# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: root = [1]
# Output: ["1"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      
      def dfs(root):
        if not root:
          return
        if not root.left and not root.right:
          tmp.append(str(root.val))
          res.append('->'.join(tmp))
          tmp.pop()
          return
        
        tmp.append(str(root.val))
        dfs(root.left)
        dfs(root.right)
        tmp.pop()
        
      res = []
      tmp = []
      dfs(root)
      return res
        