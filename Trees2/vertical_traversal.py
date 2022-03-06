# Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
# If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

# Example 1:

# Input:
#            1
#          /   \
#        2       3
#      /   \   /   \
#    4      5 6      7
#               \      \
#                8      9           
# Output: 
# 4 2 1 5 6 3 8 7 9 
# Explanation:

# Example 2:

# Input:
#        1
#     /    \
#    2       3
#  /    \      \
# 4      5      6
# Output: 4 2 1 5 3 6


from collections import deque
class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        #Your code here
        d = {}
        q = deque()
        q.append((root, 0))
        
        while q:
            node, val = q.popleft()
            if val not in d:
                d[val] = [node.data]
            else:
                d[val].append(node.data)
            
            if node.left:
                q.append((node.left, val-1))
            if node.right:
                q.append((node.right, val+1))
        
        res = []
        for i in sorted(d):
            res.extend(d[i])
        return res