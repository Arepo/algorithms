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



