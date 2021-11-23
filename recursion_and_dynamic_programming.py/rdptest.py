import timeit
import pdb

from rdp import (recursive_step_count, iterative_step_count, subsets, multiply,
                 unique_permutations, nested_arrays, flexi_arrays,
                 number_distribution, valid_parentheses)

def test_recursive_step_count():
    # Count how many paths a child running 1-3 steps up a staircase could
    # take
    assert recursive_step_count(0) == 0
    assert recursive_step_count(7) == 44

    assert iterative_step_count(0) == 0
    assert iterative_step_count(7) == 44

    recursive_runtime = timeit.timeit(
      lambda: recursive_step_count(20), number=1)
    iterative_runtime = timeit.timeit(
      lambda: iterative_step_count(20), number=1)

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
    # Create a recursive multiplication function taking two positive integers
    # without using '*' operator
    assert multiply(1,10) == 10
    assert multiply(7,6) == 42
    assert multiply(6,7) == 42
    assert multiply(3,5) == 15

def test_unique_string_permutations():
    # Compute all permutations of a string of unique characters
    assert unique_permutations('abc') == {
        'abc',
        'acb',
        'bac',
        'bca',
        'cab',
        'cba',
    }

    assert len(unique_permutations('abcdef')) == 720 # ie n!

# No big-O-optimisation attempted in this section

def test_number_distribution():
    # For a whole number num and a length length, return all the valid
    # ways of partitioning the number into t whole numbers
    assert number_distribution(num=0, length=2) == [[0,0]]
    assert number_distribution(num=1, length=3) == [
      [0,0,1],
      [1,0,0],
      [0,1,0]]

def test_nested_arrays():
    # Return all lists of length 3 that contain 0s or list, such that n
    # is the number of bracket pairs in each top-level-list
    assert nested_arrays(2) == [ [0,0,[0,0,0]], [0,[0,0,0],0], [[0,0,0],0,0] ]

def test_flexible_length_arrays():
    # Return a top level array of `size` elements and `num` bracket pairs
    assert flexi_arrays(number=1, length=1) == [[0]]
    assert flexi_arrays(number=2, length=3) == [
      [0,0,[0,0,0]],
      [0,[0,0,0],0],
      [[0,0,0],0,0]]
    assert flexi_arrays(number=2, length=2) == [[0,[0,0,0]], [[0,0,0],0]]

def test_valid_parentheses():
    # Return all valid pairings of N parentheses
    assert valid_parentheses(1) == ['()']
    assert valid_parentheses(2) == ['(())', '()()']
    assert valid_parentheses(3) == [
      '((()))', '(()())', '()(())', '(())()', '()()()']
    for_6 = valid_parentheses(6)
    # Confirm no duplicates in longer list
    assert len(set(for_6)) == len(for_6)

