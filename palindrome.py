from collections import defaultdict
import re

def is_palindrome_permutation(string):
  char_parity = defaultdict(lambda: 0)

  for char in string:
    if re.search('[a-zA-Z]', char):
      char_parity[char] ^= 1

  odd_counts = 0

  for val in char_parity.values():
    odd_counts += val
    if odd_counts > 1:
      return False
  return True

