from .propagate_rightmost_set_bit import propagate_rightmost_set_bit as pr
from .mod_power_of_two import modulo
from .check_if_power_of_two import is_2_power

def test_it_propagates_the_rightmost_set_bit_in_big_O_of_1_time():
  bit_word = int('01010000', 2)
  assert bin(pr(bit_word)) == '0b1011111'

def test_it_computes_x_mod_a_power_of_two():
  # Assuming inputs are whole numbers
  assert modulo(77, 64) == 13
  assert modulo(13, 16) == 13
  assert modulo(0,  8)  == 0
  assert modulo(10, 4)  == 2

def test_check_if_power_of_two():
  assert is_2_power(0) == False
  assert is_2_power(1) == True
  assert is_2_power(2) == True
  assert is_2_power(3) == False
  assert is_2_power(16) == True


