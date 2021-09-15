from .propagate_rightmost_set_bit import propagate_rightmost_set_bit as pr

def test_it_propagates_the_rightmost_set_bit_in_big_O_of_1_time():
  bit_word = int('01010000', 2)
  assert bin(pr(bit_word)) == '0b1011111'
