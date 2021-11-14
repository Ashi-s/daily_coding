# Design the CombinationIterator class:

# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.

# Example 1:

# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
      self.characters = characters
      self.combinationLength = combinationLength
      self.res = []
      self.N = len(characters)
      self.helper(0, [])

    def next(self) -> str:
      return self.res.pop(0)
        

    def hasNext(self) -> bool:
      return len(self.res) > 0
    
    def helper(self, idx, curr):
      if idx >= self.N and len(''.join(curr)) == self.combinationLength:
        self.res.append(''.join(curr))
        return
      if idx >= self.N:
        return
      curr.append(self.characters[idx])
      self.helper(idx+1, curr)
      
      curr.pop()
      self.helper(idx+1, curr)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()