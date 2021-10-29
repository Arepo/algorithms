from rdp import recursive_step_count, iterative_step_count
import timeit
import pdb

def test_recursive_step_count():
  """Count how many paths a child running 1-3 steps up a staircase could take"""
  assert recursive_step_count(0) == 0
  assert recursive_step_count(7) == 44

  assert iterative_step_count(0) == 0
  assert iterative_step_count(7) == 44

  recursive_runtime = timeit.timeit(lambda: recursive_step_count(20), number=1)
  iterative_runtime = timeit.timeit(lambda: iterative_step_count(20), number=1)

  assert iterative_runtime < recursive_runtime


