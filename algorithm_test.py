from .propagate_rightmost_set_bit import propagate_rightmost_set_bit as pr
from .mod_power_of_two import modulo
from .check_if_power_of_two import is_2_power
from .rectangle_functions import overlapping_rectangle, is_rectangle
from collections import namedtuple
import pdb

# All in O(1) time, using bitwise operators, rquality checks, and Boolean operators

def test_propagate_rightmost_set_bit():
  bit_word = int('01010000', 2)
  assert bin(pr(bit_word)) == '0b1011111'

def test_mod_power_of_two():
  # Assuming inputs are whole numbers
  assert modulo(77, 64) == 13
  assert modulo(13, 16) == 13
  assert modulo(0,  8)  == 0
  assert modulo(10, 4)  == 2

def test_is_2_power():
  assert is_2_power(0) == False
  assert is_2_power(1) == True
  assert is_2_power(2) == True
  assert is_2_power(3) == False
  assert is_2_power(16) == True

def test_overlapping_rectangle():
  # Do two x-/y-axis aligned rectangles overlap? If so, return the rectangle they create
  Rectangle = namedtuple('Rect', ('x', 'y', 'width', 'height'))
  rectangle_1 = Rectangle(0,0,4,3)
  rectangle_2 = Rectangle(4,3,2,3)
  rectangle_3 = Rectangle(2,2,3,5)
  rectangle_4 = Rectangle(2,4,3,3)
  rectangle_5 = Rectangle(-2,-2,3,3)
  rectangle_6 = Rectangle(-1,-1,1,1)

  assert overlapping_rectangle(rectangle_1, rectangle_2) == None
  assert overlapping_rectangle(rectangle_1, rectangle_3) == Rectangle(2,2,2,1)
  assert overlapping_rectangle(rectangle_3, rectangle_1) == Rectangle(2,2,2,1)
  assert overlapping_rectangle(rectangle_4, rectangle_2) == Rectangle(4,4,1,2)
  assert overlapping_rectangle(rectangle_5, rectangle_6) == Rectangle(-1,-1,1,1)

def test_is_rectangle():
  Point = namedtuple('Point', ('x', 'y'))
  point_1 = Point(0,0)
  point_3 = Point(3,1)
  point_2 = Point(-2,6)
  point_4 = Point(1,7)
  point_5 = Point(1,8)

  assert is_rectangle(point_1, point_2, point_3, point_4) == True
  assert is_rectangle(point_1, point_2, point_3, point_5) == False

def test_delete_dups_from_array():
  # Assumes array is sorted, and return number of 'valid' eles (can contain trailing invalid ones)
  arr = [2,3,5,5,7,11,11,11,13]
  assert uniquify(arr) == 6
  assert arr[:6] == [2,3,5,7,11,13]
