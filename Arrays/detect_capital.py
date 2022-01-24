# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 
# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

#M1 (without using any in-built functions)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
      all_small = 0
      capital = 0
      isFirstCharCapital = False
      for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
          if i == 0:
            isFirstCharCapital = True
          capital += 1
        elif 97 <= ord(word[i]) <= 122:
          all_small += 1
          
      if len(word) == capital: return True
      
      if len(word) == all_small: return True
      
      if isFirstCharCapital and len(word)-1 == all_small: return True
      
      return False

#M2 using inbuilt functions
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.isupper()):
            return True
        if(word.islower()):
            return True
        if(word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False