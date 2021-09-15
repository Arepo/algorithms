from .propagate_rightmost_set_bit import propagate_rightmost_set_bit as pr
from .mod_power_of_two import modulo

def test_it_propagates_the_rightmost_set_bit_in_big_O_of_1_time():
  bit_word = int('01010000', 2)
  assert bin(pr(bit_word)) == '0b1011111'

def test_it_computes_x_mod_a_power_of_two():
  # Assuming inputs are whole numbers
  assert modulo(77, 64) == 13
  assert modulo(13, 16) == 13
  assert modulo(0,  8)  == 0
  assert modulo(10, 4)  == 2

# original & (denom - 1)


# 1001101 % # 77
# 1000000 # 64
# 0001101

# 1001101 %
# 0000100
# 0000001

# 100 %
# 010
# 000

# 1000 %
# 0010
# 0000

# 1000 %
# 0100
# 0000

# 1111 %
# 0100
# 0011

# 1111 %
# 1000
# 0111

# 01111 %
# 10000
# 01111

# 1101 %
# 1000
# 0101

# 1001 %
# 0100
# 0001

# 10111 % # 23
# 00100
# 00011



# bin(int("0b1001101", 2) % int("0b1000000", 2))
# int("0b1101", 2)

# bin(int("0b100", 2) % int("0b010", 2))
# int("0b0", 2)

# bin(int("0b1000", 2) % int("0b0010", 2))
# int("0b0", 2)

# bin(int("0b1000", 2) %  int("0b0100", 2))
# int("0b0", 2)

# bin(int("0b1111", 2) % int("0b0100", 2))
# int("0b11", 2)

# bin(int("0b1111", 2) % int("0b1000", 2))
# int("0b111", 2)

# bin(int("0b01111", 2) % int("0b10000", 2))
# int("0b1111", 2)

# bin(int("0b1101", 2) % int("0b1000", 2))
# int("0b101", 2)

# bin(int("0b1001", 2) % int("0b0100", 2))
# int("0b1", 2)

# bin(int("0b10111", 2) % int("0b00100", 2))
# int("0b11", 2)
