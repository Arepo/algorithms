import math
import pdb

def binary_representation(num) -> str:
  bitstring = ['0', '.']
  dyadic_fractions = set()

  while num != 1:
    num = num * 2

    if num >= 1:
      dyadic_fraction = num - 1
    else:
      dyadic_fraction = num

    if (num != 1 and
       (dyadic_fraction in dyadic_fractions or
       (str(dyadic_fraction)[-1] != '5'))
    ):
      # Either we're in a loop or we know it will never multiply out to 1.0
      return "ERROR"

    dyadic_fractions.add(dyadic_fraction)
    bitstring.append(str(math.floor(num)))

  return ''.join(bitstring)

def max_1s(num) -> int:
  bitstring = f"{num:b}"
  str_start_index = 0
  substring_index = 0
  max_length = 0
  zero_index = 0

  while str_start_index < len(bitstring):

    if (
      substring_index >= len(bitstring) or
      bitstring[str_start_index] == '1' and bitstring[substring_index] == '0' and zero_index != str_start_index
    ):
      # Substring has either run off the end or reached second 0
      length = substring_index - str_start_index
      max_length = max(max_length, length)
      str_start_index = substring_index = zero_index + 1
      zero_index = str_start_index

    elif bitstring[str_start_index] == '1' and bitstring[substring_index] == '1':
      substring_index += 1

    elif bitstring[str_start_index] == '1':
      # Bit is the first 0 we've encountered
      zero_index = substring_index
      substring_index += 1

    else:
      # Str start is a 0
      str_start_index = substring_index = zero_index + 1
      zero_index = str_start_index


  return max_length

def count_bit_transitions(num1, num2) -> int:
  exclusive_bits = num1 ^ num2
  transitions = 0
  while exclusive_bits != 0:
    transitions += 1
    exclusive_bits = exclusive_bits & (exclusive_bits - 1)
  return transitions

def draw_line(screen, screen_width, x1, x2, y):
  first_byte_index = _bytes_index(screen, screen_width, x1, y)
  last_byte_index = _bytes_index(screen, screen_width, x2, y)

  if first_byte_index == last_byte_index:
    screen[first_byte_index] = screen[first_byte_index] | (255 >> (_byte_index(x1) + 7 - _byte_index(x2))) << 7 - _byte_index(x2)
  else:
    screen[first_byte_index] = screen[first_byte_index] | 255 & ~(255 << 8 - _byte_index(x1))

    for byte in range(first_byte_index + 1, last_byte_index):
      # Intermediate bytes are all 1s
      screen[byte] = 255

    screen[last_byte_index] = screen[last_byte_index] | 255 & (255 << 8 - _byte_index(x2))


def _bytes_index(screen, width, x, y):
  height = int(len(screen) / width - 1)
  return int(x / 8) + width * (height - y)

def _byte_index(x):
  return x % 8

