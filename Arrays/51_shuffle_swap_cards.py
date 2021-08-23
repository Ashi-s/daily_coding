# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a function that generates perfectly random numbers between 1 and k (inclusive),
# where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

# It should run in O(N) time.

# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

from random import randint

SIZE = 52

def generate_random(k):
  return randint(0, k)


def shuffle_cards():
  cards = [i for i in range(SIZE)]

  for old_pos in cards:
    new_pos = old_pos + generate_random(SIZE - old_pos - 1)
    cards[old_pos], cards[new_pos] = cards[new_pos], cards[old_pos]

  return cards

print(shuffle_cards())