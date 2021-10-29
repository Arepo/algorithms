import pdb

def recursive_step_count(n):
  if n < 3:
    return n
  if n == 3:
    return 4
  return recursive_step_count(n - 1) + recursive_step_count(n - 2) + recursive_step_count(n - 3)

def iterative_step_count(n):
  if n < 3:
    return n
  a = 1
  b = 1
  c = 2
  for _ in range(n - 3):
    d = a + b + c # 4
    a = b
    b = c
    c = d
  return a + b + c
