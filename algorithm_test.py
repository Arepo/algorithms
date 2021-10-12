from .propagate_rightmost_set_bit import propagate_rightmost_set_bit as pr
from .mod_power_of_two import modulo
from .check_if_power_of_two import is_2_power
from .rectangle_functions import overlapping_rectangle, is_rectangle
from .remove_key import remove_key
from .primes import primes_to_n
from .palindrome import is_palindrome_permutation
from .is_one_away import is_one_away
from .matrix_rotation import rotate
from .linked_list import SinglyLinkedList
from .node import Node
from .stack_array_manager import StackArrayManager
from collections import namedtuple
import pdb

def test_propagate_rightmost_set_bit():
  # In O(1) time, using bitwise operators, equality checks, and Boolean operators
  bit_word = int('01010000', 2)
  assert bin(pr(bit_word)) == '0b1011111'

def test_mod_power_of_two():
  # In O(1) time, using bitwise operators, equality checks, and Boolean operators
  # Assuming inputs are whole numbers
  assert modulo(77, 64) == 13
  assert modulo(13, 16) == 13
  assert modulo(0,  8)  == 0
  assert modulo(10, 4)  == 2

def test_is_2_power():
  # In O(1) time, using bitwise operators, equality checks, and Boolean operators
  assert is_2_power(0) == False
  assert is_2_power(1)
  assert is_2_power(2)
  assert is_2_power(3) == False
  assert is_2_power(16)

def test_overlapping_rectangle():
  # Do two x-/y-axis aligned rectangles overlap? If so, return the rectangle they create
  Rectangle = namedtuple('Rect', ('x', 'y', 'width', 'height'))
  rectangle_1 = Rectangle(0, 0, 4, 3)
  rectangle_2 = Rectangle(4, 3, 2, 3)
  rectangle_3 = Rectangle(2, 2, 3, 5)
  rectangle_4 = Rectangle(2, 4, 3, 3)
  rectangle_5 = Rectangle(-2, -2, 3, 3)
  rectangle_6 = Rectangle(-1, -1, 1, 1)

  assert overlapping_rectangle(rectangle_1, rectangle_2) == None
  assert overlapping_rectangle(rectangle_1, rectangle_3) == Rectangle(2, 2, 2, 1)
  assert overlapping_rectangle(rectangle_3, rectangle_1) == Rectangle(2, 2, 2, 1)
  assert overlapping_rectangle(rectangle_4, rectangle_2) == Rectangle(4, 4, 1, 2)
  assert overlapping_rectangle(rectangle_5, rectangle_6) == Rectangle(-1, -1, 1, 1)

def test_is_rectangle():
  Point = namedtuple('Point', ('x', 'y'))
  point_1 = Point(0, 0)
  point_3 = Point(3, 1)
  point_2 = Point(-2, 6)
  point_4 = Point(1, 7)
  point_5 = Point(1, 8)

  assert is_rectangle(point_1, point_2, point_3, point_4)
  assert is_rectangle(point_1, point_2, point_3, point_5) == False

# Array/string algorithms

def test_remove_key():
  # Modify array and return number of elements remaining in O(n) time and O(1) space, left-shifting valid values and leaving invalid ones afterwards
  arr = [1, 1, 1]
  assert remove_key(arr, 1) == 0
  assert arr == [1, 1, 1]

  arr = [1, 1, 2]
  assert remove_key(arr, 1) == 1
  assert arr[:1] == [2]

  arr = [1, 2, 2]
  assert remove_key(arr, 1) == 2
  assert arr[:2] == [2, 2]

  arr = [2, 2, 2]
  assert remove_key(arr, 1) == 3
  assert arr == [2, 2, 2]

  arr = [2, 1, 1]
  assert remove_key(arr, 1) == 1
  assert arr[:1] == [2]

  arr = [2, 2, 1]
  assert remove_key(arr, 1) == 2
  assert arr[:2] == [2, 2]

  arr = [13, 11, 11, 11, 5, 2, 5, 11, 3,'a', 5, 5]
  assert remove_key(arr, 11) == 8
  assert arr[:8] == [13, 5, 2, 5, 3, 'a', 5, 5]

def test_primes_to_n():
  primes = primes_to_n(1000)
  assert all(prime in primes for prime in [2, 109, 523, 997])
  assert all(nonprime not in primes for nonprime in [1, 4, 555, 1000])

def test_is_permutation_of_palindrome():
  palindromic, non_palindromic = 'aa bb ccc', 'aa bbb ccc'
  assert is_palindrome_permutation(palindromic)
  assert is_palindrome_permutation(non_palindromic) == False

def test_is_one_away():
  # return true if StringA requires 1 or 0 edits to match StringB
  assert is_one_away('pale', 'ple')
  assert is_one_away('pales', 'pale')
  assert is_one_away('pale', 'bale')
  assert is_one_away('pale', 'bake') == False

def test_matrix_rotation():
  # In place rotation
  odd_matrix = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
  rotate(odd_matrix)
  assert odd_matrix == [[7, 4, 1],
                        [8, 5, 2],
                        [9, 6, 3]]

  even_matrix =[['a', 'b', 'c', 'd'],
                ['e', 'f', 'g', 'h'],
                ['i', 'j', 'k', 'l'],
                ['m', 'n', 'o', 'p']]
  rotate(even_matrix)
  assert even_matrix  == [['m', 'i', 'e', 'a'],
                          ['n', 'j', 'f', 'b'],
                          ['o', 'k', 'g', 'c'],
                          ['p', 'l', 'h', 'd']]



class TestSinglyLinkedListFunctions:
  def build_list_to_n(self, sll, n):
    for i in range(0, n):
      sll.append(Node(i))

  def test_kth_from_end(self):
    sll = SinglyLinkedList()
    self.build_list_to_n(sll, 10)
    assert sll.kth_from_end(1).data == 9
    assert sll.kth_from_end(7).data == 3

  def test_is_palindrome(self):
    # Given list length
    non_palindrome = SinglyLinkedList()
    odd_palindrome = SinglyLinkedList()
    even_palindrome = SinglyLinkedList()

    for char in 'abracadabra':
      non_palindrome.append(Node(char))
    for char in 'aba':
      odd_palindrome.append(Node(char))
    for char in 'redder':
      even_palindrome.append(Node(char))

    assert non_palindrome.is_palindrome(length=11) == False
    assert odd_palindrome.is_palindrome(length=3)
    assert even_palindrome.is_palindrome(length=6)

  def test_intersecting_node(self):
    # Get intersecting node in O(N + M) time, O(1) space
    list1,list2, list3 = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
    nodes = {}
    for i in range(1, 5):

      nodes[f'node {i}'] = Node(i)

      list1.append(nodes[f'node {i}'])

    for i in range(1, 5):
      list3.append(Node(i))

    list2.head = nodes['node 3']
    list2.push(Node(0))

    assert list1.intersecting_node(list2) == nodes['node 3']
    assert list1.intersecting_node(list3) == None

  def test_find_loop_node(self):
    # Get node at start of loop if there is one
    looping_list, terminating_list = SinglyLinkedList(), SinglyLinkedList()
    # pdb.set_trace()
    self.build_list_to_n(looping_list, 5)
    self.build_list_to_n(terminating_list, 5)
    looping_node = Node(5)
    looping_list.append(looping_node)
    looping_node.next = looping_list.head.next

    assert looping_list.find_loop_node() == looping_list.head.next
    assert terminating_list.find_loop_node() == None

# Stack & Queue tests

def test_3_stack_array():
  # Implement three stacks with a single array
  manager = ArrayStackManager()
  for i in range(0,3):
    assert manager.is_empty(stack=i) == True
    manager.push(stack=i, val=i * 3)

  for i in range(0,3):
    assert manager.is_empty(stack=i) == False
    assert manager.peek(stack=i) == i * 3
    assert manager.pop(stack=i) == i * 3

  for i in range(0,3):
    assert manager.is_empty(stack=i) == True
