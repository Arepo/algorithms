from rdp import recursive_step_count, iterative_step_count, subsets, multiply
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
  assert subsets({1}) == {frozenset(), frozenset({1})}
  assert subsets({1,2,3,4,5}) == {
    frozenset(),
    frozenset({1}),
    frozenset({2}),
    frozenset({3}),
    frozenset({4}),
    frozenset({5}),
    frozenset({1,2}),
    frozenset({1,3}),
    frozenset({1,4}),
    frozenset({1,5}),
    frozenset({2,3}),
    frozenset({2,4}),
    frozenset({2,5}),
    frozenset({3,4}),
    frozenset({3,5}),
    frozenset({4,5}),
    frozenset({1,2,3}),
    frozenset({1,2,4}),
    frozenset({1,2,5}),
    frozenset({1,3,4}),
    frozenset({1,3,5}),
    frozenset({1,4,5}),
    frozenset({2,3,4}),
    frozenset({2,3,5}),
    frozenset({2,4,5}),
    frozenset({3,4,5}),
    frozenset({1,2,3,4}),
    frozenset({1,2,3,5}),
    frozenset({1,2,4,5}),
    frozenset({1,3,4,5}),
    frozenset({2,3,4,5}),
    frozenset({1,2,3,4,5})
  }

def test_recursive_multiplication():
  # Create a recursive multiplication function taking two positive integers without using '*' operator
  assert multiply(1,10) == 10
  assert multiply(7,6) == 42
  assert multiply(6,7) == 42
  assert multiply(3,5) == 15
