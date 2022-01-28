# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

# Example:

# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
 

class Trie:
  def __init__(self):
    self.children = {}
    self.isEnd = False
class WordDictionary:

    def __init__(self):
      self.root = Trie()
        

    def addWord(self, word: str) -> None:
      curr = self.root
      for i in range(len(word)):
        if word[i] not in curr.children:
          curr.children[word[i]] = Trie()
          
        curr = curr.children[word[i]]
        
        if i == len(word) - 1:
          curr.isEnd = True

    def search(self, word: str) -> bool:
      
      def dfs(i, trav):
        if i == len(word):
            return trav.isEnd
        if word[i] != ".":
            if word[i] not in trav.children:
                return False
            else:
                return dfs(i+1, trav.children[word[i]])
        else:
            for val in trav.children.values():
                if dfs(i+1, val):
                    return True
            return False
      return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)