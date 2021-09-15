def propagate_rightmost_set_bit(n: int) -> int:
  subtracted = n - 1
  return n | subtracted
