# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Example 1:


# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# Example 2:


# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
      res = []

      def helper(root):
        if root:
          helper(root.left)
          res.append(root.val)
          helper(root.right)
      
      if root1:
        helper(root1)
      if root2:
        helper(root2)
      
      res.sort()
      return res

def traverse(root):
  if root:
    traverse(root.left)
    print(root.val)
    traverse(root.right)



T = TreeNode(0)
T.left = TreeNode(-10)
T.right = TreeNode(10)

T1 = TreeNode(5)
T1.left = TreeNode(1)
T1.right = TreeNode(7)
T1.left.left = TreeNode(0)
T1.left.right = TreeNode(2)
print(traverse(T))
print(traverse(T1))




[0,-10,10]
[5,1,7,0,2,6,10]