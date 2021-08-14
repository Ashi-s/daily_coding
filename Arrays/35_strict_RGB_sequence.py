# This problem was asked by Google.

# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def strict_RGB_sequence(s):
  count = 0
  for i in range(len(s)):
    if s[i] == 'R':
      s[count], s[i] = s[i], s[count]
      count += 1
  
  for j in range(count, len(s)):
    if s[j] == 'G':
      s[count], s[j] = s[j], s[count]
      count += 1

  return s

print(strict_RGB_sequence(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(strict_RGB_sequence((['G', 'B', 'R'])))
print(strict_RGB_sequence(([ 'B', 'R', 'G'])))