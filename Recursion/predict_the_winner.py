# You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

# Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0.
#  At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
#  which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

# Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, 
# and you should also return true. You may assume that both players are playing optimally.

 

# Example 1:

# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return false.
# Example 2:

# Input: nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

      def helper(arr, score1, score2, isp1):
        if len(arr) == 0:
          return score1 >= score2
    
        if isp1:
          res = helper(arr[1:], score1 + arr[0], score2, not isp1) or helper(arr[:-1], score1 + arr[-1], score2, not isp1)
          return res
        else:
          res = helper(arr[1:], score1 , score2 + arr[0], not isp1) and helper(arr[:-1], score1, score2 + arr[-1], not isp1)
          return res
        
      return helper(nums, 0, 0, True)


#for refernce M2
def PredictTheWinner(self, nums):
        
        def canWin(nums, player1, player2, is1Turn):
            if not nums:
                if (player1 >= player2 and is1Turn) or (player2 > player1 and not is1Turn):
                    return True
                else:
                    return False
                
            if is1Turn:
                return not canWin(nums[1:], player1 + nums[0], player2, not is1Turn) or not canWin(nums[:len(nums) - 1], player1 + nums[-1], player2, not is1Turn)
            else:
                return not canWin(nums[1:], player1, player2 + nums[0], not is1Turn) or not canWin(nums[:len(nums) - 1], player1, player2 + nums[-1], not is1Turn)
        
        return canWin(nums, 0, 0, True)