# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a
#  sequence of push and pop operations on an initially empty stack, or false otherwise.

 

# Example 1:

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# Example 2:

# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

def validateStackSequences( pushed, popped):
  if len(pushed) == 0 or len(popped) == 0:
    return True
  i, j = 1, 0
  st = [pushed[0]]
  
  while i < len(pushed)+1:
    if st and st[-1] == popped[j]:
      st.pop()
      j += 1
    else:
      if i < len(pushed):
        st.append(pushed[i])
        i += 1
      else:
        return len(st) == 0
  return len(st) == 0

pushed = [4,5,1,2,3]
popped = [4,3,5,1,2]

pushed1 = [1,2,3,4,5]
popped1 = [4,5,3,2,1]

print(validateStackSequences(pushed1, popped1))