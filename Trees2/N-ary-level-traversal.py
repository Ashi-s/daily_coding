# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

# Example 1:



# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
# Example 2:



# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

import queue
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      if not root:
        return []
      q = queue.Queue()
      q.put(root)
      res = []
      
      while not q.empty():
        size = q.qsize()
        temp = []
        while size > 0:
          node = q.get()
          temp.append(node.val)
          for c in node.children:
            q.put(c)
          size -= 1
        res.append(temp)
      return res
        