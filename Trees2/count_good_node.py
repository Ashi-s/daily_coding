# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      if not root:
        return 0
      self.count = 1
      self.helper( root, root.val)
      return self.count
    
    def helper(self,root, max_path):
      if not root:
        return
      
      if root.left:
        temp = max_path
        if root.left.val >= max_path:
          self.count += 1
          max_path = root.left.val

        self.helper(root.left, max_path)
        max_path = temp

      if root.right:
        temp = max_path
        if root.right.val >= max_path:
          self.count += 1
          max_path = root.right.val

        self.helper(root.right, max_path)
        max_path = temp
    
      
root = TreeNode(3)
n1 = TreeNode(1)
n2 = TreeNode(4)

n3 = TreeNode(3)
n4 = TreeNode(1)
n5 = TreeNode(5)

root.left = n1
root.right = n2

root.left.left = n3

root.right.left = n4
root.right.right = n5

print(goodNodes(root))


