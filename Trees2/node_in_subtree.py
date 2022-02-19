# You are given a tree that contains N nodes, each containing an integer u which corresponds to a lowercase character c in the string s using 1-based indexing.
# You are required to answer Q queries of type [u, c], where u is an integer and c is a lowercase letter. The query result is the number of nodes in the subtree of node u containing c.
# Signature
# int[] countOfNodes(Node root, ArrayList<Query> queries, String s)
# Input
# A pointer to the root node, an array list containing Q queries of type [u, c], and a string s
# Constraints
# N and Q are the integers between 1 and 1,000,000
# u is a unique integer between 1 and N
# s is of the length of N, containing only lowercase letters
# c is a lowercase letter contained in string s
# Node 1 is the root of the tree
# Output
# An integer array containing the response to each query
# Example
#         1(a)
#         /   \
#       2(b)  3(a)
# s = "aba"
# RootNode = 1
# query = [[1, 'a']]
# Note: Node 1 corresponds to first letter 'a', Node 2 corresponds to second letter of the string 'b', Node 3 corresponds to third letter of the string 'a'.
# output = [2]
# Both Node 1 and Node 3 contain 'a', so the number of nodes within the subtree of Node 1 containing 'a' is 2.


import math
# Add any extra import statements you may need here


class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

# Add any helper functions you may need here


def count_of_nodes(root, queries, s):
  def getRoot(root, n):
    nonlocal nodeMatched
    if root and root.val == n:
      nodeMatched = root
      return
    # if not root.children: return
    for c in root.children:
      getRoot(c, n)

  def getCommon(root, s, val, res):
    # if not root.children: return
    for c in root.children:
      if s[c.val-1] == val:
        res.append(1)
      getCommon(c, s, val, res)
  # Write your code here
  output = []
  for n, val in queries:
    nodeMatched = Node(0)
    getRoot(root, n)
    node = nodeMatched 
    print('root.val ', n, val, nodeMatched.val)
    res = []
    if s[node.val-1] == val:
      res.append(1)
    getCommon(node, s, val, res)
    output.append(sum(res))
  return output



s_2 = "abaacab"
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [(1, 'a'),(2, 'b'),(3, 'a')]

print(count_of_nodes(root_2, queries_2, s_2)) # [4, 1, 2]