# Minimizing Permutations

# In this problem, you are given an integer N, and a permutation, P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N). You want to rearrange the elements of the permutation into increasing order, repeatedly making the following operation:
# Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
# Your goal is to compute the minimum number of such operations required to return the permutation to increasing order.

# Signature
# int minOperations(int[] arr)

# Input
# Array arr is a permutation of all integers from 1 to N, N is between 1 and 8

# Output
# An integer denoting the minimum number of operations required to arrange the permutation in increasing order

# Example
# If N = 3, and P = (3, 1, 2), we can do the following operations:
# Select (1, 2) and reverse it: P = (3, 2, 1).
# Select (3, 2, 1) and reverse it: P = (1, 2, 3).
# output = 2

from queue import Queue
def minimizePerm(num):
  final = ''.join(sorted([str(i) for i in num]))
  num = ''.join([str(i) for i in num])
  visited = set()
  q = Queue()
  q.put((num, 0))

  while not q.empty():
    word, count = q.get()

    if word == final:
      return count
    
    for i in range(len(word)):
      for j in range(i, len(word)):
        tmp = word[:i] +  word[i:j+1][::-1] + word[j+1:]

        if tmp not in visited:
          q.put((tmp, count+1))
          visited.add(tmp)
  
  return -1

print(minimizePerm([3,1,2]))
  
