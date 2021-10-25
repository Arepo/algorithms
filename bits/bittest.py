import pdb

from real_numbers import binary_representation

def test_binary_representation():
  # Assume 0 <= input < 1
  assert binary_representation(0.5) == '0.1'
  assert binary_representation(0.125) == '0.001'
  assert binary_representation(0.79) == 'ERROR'
