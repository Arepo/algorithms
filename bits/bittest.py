import pdb

from bit_functions import binary_representation, max_1s, bit_transitions

def test_binary_representation():
  # Assume 0 <= input < 1
  assert binary_representation(0.5) == '0.1'
  assert binary_representation(0.125) == '0.001'
  assert binary_representation(0.79) == 'ERROR'

def test_max_1s():
  # Return the max consecutive 1s you could create with a single flip on the bit sequence of an integer
  assert max_1s(9) == 2
  # assert max_1s(1775) == 8

def test_bit_transitions():
  # Return number of flipped bits necessary to turn num A to num B
  assert bit_transitions(29, 15) == 2
  assert bit_transitions(35, 24) == 5
