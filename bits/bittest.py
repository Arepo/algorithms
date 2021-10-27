import pdb

from bit_functions import binary_representation, max_1s, count_bit_transitions, draw_line

def test_binary_representation():
  # Assume 0 <= input < 1
  assert binary_representation(0.5) == '0.1'
  assert binary_representation(0.125) == '0.001'
  assert binary_representation(0.79) == 'ERROR'

def test_max_1s():
  # Return the max consecutive 1s you could create with a single flip on the bit sequence of an integer
  assert max_1s(9) == 2
  # assert max_1s(1775) == 8

def test_count_bit_transitions():
  # Return number of flipped bits necessary to turn num A to num B
  assert count_bit_transitions(29, 15) == 2
  assert count_bit_transitions(35, 24) == 5

def test_draw_line():
  # Set all bits in a line represented by a bitarray, representing a monochrome screen
  display = [
    0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0
  ]
  draw_line(display, screen_width=8, x1=19, x2=53, y=1)
  draw_line(display, screen_width=8, x1=5, x2=40, y=2)
  assert display == [
    False
  ]
