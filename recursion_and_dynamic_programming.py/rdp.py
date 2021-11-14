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

def unique_permutations(string: str) -> set:
  substring_permutations = set()

  if len(string) == 1:
    substring_permutations.add(string)
    return substring_permutations

  for substring in unique_permutations(string[1:]):
    for i in range(len(substring) + 1):
      substring_permutations.add(substring[:i] + string[0] + substring[i:])
  return substring_permutations


def nested_arrays(num):
  if num == 0:
    return [0]

  subarrays = []
  for eye in range(num):
    for jay in range(num-eye):
      for i_ele in nested_arrays(eye):
        for j_ele in nested_arrays(jay):
          for k_ele in nested_arrays(num-1-eye-jay):
            subarrays.append(
              [i_ele, j_ele,  k_ele]
            )
  return subarrays

def number_distribution(num, length):
  def add_distributions(subdistributions, distributions, remainder):
    if not subdistributions:
      return
    distributions.append(subdistributions.pop() + [remainder])
    add_distributions(subdistributions, distributions, remainder)

  if length == 0:
    return [] # Should only reach this branch with an original value of 0
  if length == 1:
    return [[num]]
  distributions = []
  for eye in range(num + 1):
    add_distributions(
      number_distribution(eye, length - 1),
      distributions,
      num - eye
    )
  return distributions

def flexi_arrays(number,length):
  if number == 0:
    return [0]
  if number == 1 and length == 0:
    return [[]]
  if length == 0:
    return []

  results = []
  for eye in range(1, number + 1):
    for prefix in flexi_arrays(eye, length - 1):
      for suffix in flexi_arrays(number - eye, 3):
        results.append(prefix + [suffix])
  return results

def valid_parentheses(magnitude):
  if magnitude == 0:
    return ['']

  results = []
  for eye in range(magnitude):
    for prefix in valid_parentheses(eye):
      for suffix in valid_parentheses(magnitude - eye - 1):
        for enclosed_suffix in ['(' + suffix + ')' ]:
          results.append(prefix + enclosed_suffix)
  return results




