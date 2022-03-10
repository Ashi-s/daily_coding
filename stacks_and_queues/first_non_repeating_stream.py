# Given an input stream of A of n characters consisting only of lower case alphabets. The task is to find the first non repeating character, 
# each time a character is inserted to the stream. If there is no such character then append '#' to the answer.
 

# Example 1:

# Input: A = "aabc"
# Output: "a#bb"
# Explanation: For every character first non
# repeating character is as follow-
# "a" - first non-repeating character is 'a'
# "aa" - no non-repeating character so '#'
# "aab" - first non-repeating character is 'b'
# "aabc" - first non-repeating character is 'b'
# Example 2:

# Input: A = "zz"
# Output: "z#"
# Explanation: For every character first non
# repeating character is as follow-
# "z" - first non-repeating character is 'z'
# "zz" - no non-repeating character so '#'

from collections import deque
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		d = [ 0 for _ in range(26)]
		q = deque()
		q.append(A[0])
		d[ord(A[0])-ord('a')] = 1
		res = A[0]
		for c in range(1, len(A)):
            d[ord(A[c])-ord('a')] += 1
            
            
            while q and d[ord(q[0])-ord('a')] > 1:
                q.popleft()
            if len(q) == 0 and d[ord(A[c])-ord('a')] == 1:
                res += A[c]
            else:
                if len(q) == 0:
                    res += '#'
                else:
                    res += q[0]
            q.append(A[c])
        
        return res