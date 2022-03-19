# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false


#TLE
def word_break(s, wordDict):
  wordDict = set(wordDict)

  result = False
  def helper(idx, word, s, wordDict):
    nonlocal result
    if idx == len(s):
      result = True
      return
    
    if idx > len(s):
      return

    if s[idx: idx+len(word)] in wordDict:
      for next_word in wordDict:
        helper(idx+len(word), next_word, s, wordDict)

  for word in wordDict:
    helper(0, word, s, wordDict)
  
  return result

s = "leetcode"
wordDict = ["leet","code"]
s1 = "applepenapple"
wordDict1 = ["apple","pen"]
s2 = "catsandog"
wordDict2 = ["cats","dog","sand","and","cat"]

print(word_break(s, wordDict))
print(word_break(s1, wordDict1))
print(word_break(s2, wordDict2))


