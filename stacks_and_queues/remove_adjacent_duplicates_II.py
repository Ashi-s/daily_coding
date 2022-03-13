# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, 
# causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"



# M1 TLE
def remove_dup(st, k):
  if ''.join(st[-k:]) == st[-1] * k:
    for _ in range(k):
      st.pop()

def removeDuplicates(s, k):
  st = [s[0]]
  for i in range(1, len(s)):
    if len(st) >= k:
      remove_dup(st, k)
    st.append(s[i])
  
  #check last 
  remove_dup(st, k)
  return ''.join(st)


#M2
def removeDuplicates2(s, k):
  prev = ''
  count = 0
  st = []

  for i in range(len(s)):
    if not prev:
      count = 1
      prev = s[i]
    elif prev == s[i]:
      count += 1
      if count == k:
        if not st:
          prev, count = '', 0
        else:
          prev, count = st.pop()
    else:
      st.append((prev, count))
      prev = s[i]
      count = 1
  
  st.append((prev, count))
  res = ''
  for char, val in st:
    res += char * val
  
  return res


s1 = "abcd"
k1 = 2

s2 = "deeedbbcccbdaa"
k2 = 3

s3 = "wilddddddddddgooowwwwwwwwwwoooossssssssssoccccccchhhhhhhhhhcccccccccccccooryyyyyyyffffffffffyyynaicv"
k3 = 10
print(removeDuplicates2(s1, k1))
print(removeDuplicates2(s2, k2))
print(removeDuplicates2(s3, k3))