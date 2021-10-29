from rdp import recursive_step_count, iterative_step_count, subsets
import timeit
import pdb

def test_recursive_step_count():
  # Count how many paths a child running 1-3 steps up a staircase could take
  assert recursive_step_count(0) == 0
  assert recursive_step_count(7) == 44

  assert iterative_step_count(0) == 0
  assert iterative_step_count(7) == 44

  recursive_runtime = timeit.timeit(lambda: recursive_step_count(20), number=1)
  iterative_runtime = timeit.timeit(lambda: iterative_step_count(20), number=1)

  assert iterative_runtime < recursive_runtime

def test_subsets():
  # return all subsets of a set
  assert subsets({1}) == {set(), {1}}
  assert subsets({1,2,3,4,5}) == {
    set(),
    {1},
    {2},
    {3},
    {4},
    {5},
    {1,2},
    {1,3},
    {1,4},
    {1,5},
    {2,3},
    {2,4},
    {2,5},
    {3,4},
    {3,5},
    {4,5},
    {1,2,3},
    {1,2,4},
    {1,2,5},
    {1,3,4},
    {1,3,5},
    {1,4,5},
    {2,3,4},
    {2,3,5},
    {2,4,5},
    {3,4,5},
    {1,2,3,4},
    {1,2,3,5},
    {1,2,4,5},
    {1,3,4,5},
    {2,3,4,5},
    {1,2,3,4,5}
  }
