import math
import pdb

def binary_representation(num):
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

def max_1s(num):
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


