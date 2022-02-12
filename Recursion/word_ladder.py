# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

#M1 Recursion (TLE)
def ladderLength(beginWord, endWord, wordList):
  def helper(begin, end, visited, curr, res):
    if begin == end:
      res.append(sum(curr))
      return
    
    for word in wordList:
      if word not in visited:
        if diff(begin, word):
          visited.append(word)
          curr.append(1)
          helper(word, end, visited, curr, res)
          visited.pop()
          curr.pop()
  
  def diff(word1, word2):
    count = 0
    for i,j in zip(word1, word2):
      if i == j:
        continue
      else:
        count += 1
      
      if count > 1:
        return False
    
    return count
  
  res = []
  helper(beginWord, endWord, [], [], res)
  return min(res) + 1 if len(res) > 0 else 0

# beginWord = "qa"
# endWord = "sq"
# wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

beginWord = 'hit'
endWord = 'cog'
wordList = ["hot","dot","dog","lot","log","cog"]


#M2 Queue
from queue import Queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
      wordList = set(wordList)
      q = Queue()
      q.put((beginWord, 1))
      visited = set()
      
      while not q.empty():
        word, dist = q.get()
        if word == endWord:
          return dist
        for i in range(len(word)):
          for j in 'abcdefghijklmnopqrstuvwxyz':
            tmp = word[:i] + j + word[i+1:]
            if tmp not in visited and tmp in wordList:
              q.put((tmp, dist+1))
              visited.add(tmp)
      
      return 0
print(ladderLength1(beginWord, endWord, wordList))