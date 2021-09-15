def is_2_power(num: int) -> bool:
  return num != 0 and num & (num - 1) == 0
