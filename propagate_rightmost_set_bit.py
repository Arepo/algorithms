def propagate_rightmost_set_bit(n: int) -> int:
  subtracted = n - 1
  xored = n ^ subtracted
  return n | xored

# 01010000 - 1
# 01001111 XOR both
# 00011111 OR with first

