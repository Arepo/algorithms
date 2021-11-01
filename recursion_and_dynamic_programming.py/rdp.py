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

def subsets(superset):
  def subsets(superset, memo):
    if superset in memo:
      return

    memo.add(frozenset(superset))
    for ele in superset:
      subsets(superset - {ele}, memo)

  memo = set()
  subsets(superset, memo)
  return memo

def multiply(x,y):
  def multiply(x,y,log2_of_y):
    if y < 1:
      return 0
    if y == 1:
      return x
    if x == 1:
      return y
    if log2_of_y:
      return x << log2_of_y

    highest_included_power_of_2 = 0
    while y >> highest_included_power_of_2 + 1:
      highest_included_power_of_2 += 1
    remaining_multiple = y - (1 << highest_included_power_of_2)

    return multiply(x, y, highest_included_power_of_2) + multiply(x, remaining_multiple, 0)

  return multiply(x,y,0)

def permutations(string: str) -> set:
  def get_substring_permutations(string: str) -> set:
    substring_permutations = set()

    if len(string) == 1:
      substring_permutations.add(string)
      return substring_permutations

    for substring in get_substring_permutations(string[1:]):
      for i in range(len(substring) + 1):
        substring_permutations.add(substring[:i] + string[0] + substring[i:])
    return substring_permutations

  return get_substring_permutations(string)



